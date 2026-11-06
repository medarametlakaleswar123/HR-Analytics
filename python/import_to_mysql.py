
import pandas as pd
import os

from pathlib import Path
from dotenv import load_dotenv

from sqlalchemy import create_engine, URL, text, inspect


# ============================================
# 1. PROJECT PATHS
# ============================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = (
    BASE_DIR /
    "data" /
    "cleaned" /
    "cleaned_hr.csv"
)

ENV_PATH = BASE_DIR / ".env"


# ============================================
# 2. LOAD ENVIRONMENT VARIABLES
# ============================================

load_dotenv(ENV_PATH)

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


# ============================================
# 3. VALIDATE CONFIGURATION
# ============================================

if not all([
    DB_HOST,
    DB_PORT,
    DB_USER,
    DB_PASSWORD,
    DB_NAME
]):

    raise ValueError(
        "Missing database configuration. "
        "Check your .env file."
    )


# ============================================
# 4. LOAD CLEANED DATASET
# ============================================

if not DATA_PATH.exists():

    raise FileNotFoundError(
        f"Cleaned dataset not found: {DATA_PATH}"
    )

df = pd.read_csv(DATA_PATH)

print("\n========== DATASET LOADED ==========")

print("Total Records:", len(df))

print("Total Columns:", len(df.columns))


# ============================================
# 5. VALIDATE DATA
# ============================================

if df["EmployeeNumber"].isnull().any():

    raise ValueError("EmployeeNumber contains NULL values.")

if df["EmployeeNumber"].duplicated().any():

    raise ValueError("Duplicate EmployeeNumber values found.")

if df.isnull().sum().sum() > 0:

    raise ValueError(
        "Missing values detected. Run data_cleaning.py again."
    )


# ============================================
# 6. CREATE MYSQL CONNECTION
# ============================================

connection_url = URL.create(
    drivername="mysql+pymysql",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=int(DB_PORT),
    database=DB_NAME
)

engine = create_engine(
    connection_url,
    echo=False
)

print("\n========== MYSQL CONNECTION ==========")


# ============================================
# 7. CHECK DATABASE TABLE
# ============================================

inspector = inspect(engine)

if not inspector.has_table("hr_employee"):

    raise ValueError(
        "hr_employee table not found. "
        "Execute sql/database.sql first."
    )

print("MySQL Connection Successful!")

print("Database:", DB_NAME)

print("Table: hr_employee")


# ============================================
# 8. VERIFY COLUMN STRUCTURE
# ============================================

mysql_columns = [
    column["name"]
    for column in inspector.get_columns("hr_employee")
]

missing_columns = [
    column for column in df.columns
    if column not in mysql_columns
]

if missing_columns:

    raise ValueError(
        f"CSV columns missing from MySQL table: {missing_columns}"
    )

if set(df.columns) != set(mysql_columns):

    raise ValueError(
        "CSV and MySQL table columns do not match."
    )


# ============================================
# 9. IMPORT DATA INTO MYSQL
# ============================================

print("\n========== IMPORTING DATA ==========")

# Clear previous rows so rerunning the script
# does not create duplicate primary-key records.

with engine.begin() as connection:

    connection.execute(
        text("DELETE FROM hr_employee")
    )

    df.to_sql(
        name="hr_employee",
        con=connection,
        if_exists="append",
        index=False,
        chunksize=500
    )

print("Data imported successfully!")


# ============================================
# 10. VERIFY IMPORTED RECORDS
# ============================================

with engine.connect() as connection:

    total_records = connection.execute(
        text("SELECT COUNT(*) FROM hr_employee")
    ).scalar_one()

    print("\n========== IMPORT VERIFICATION ==========")

    print("Total Records Imported:", total_records)

    result = connection.execute(
        text("SELECT * FROM hr_employee LIMIT 5")
    )

    print("\nFIRST 5 RECORDS:")

    for row in result:

        print(row)


# ============================================
# 11. FINAL STATUS
# ============================================

if total_records != len(df):

    raise ValueError(
        "Imported record count does not match CSV record count."
    )

print("\n========== IMPORT COMPLETED ==========")

print("CSV Records:", len(df))

print("MySQL Records:", total_records)

print("Database:", DB_NAME)

print("Table: hr_employee")

engine.dispose()
