
import pandas as pd
import numpy as np
from pathlib import Path

# ============================================
# 1. PROJECT PATHS
# ============================================

BASE_DIR=Path(__file__).resolve().parent.parent

RAW_PATH = BASE_DIR / "data" / "raw" / "HR-Employee-Attrition.csv"

CLEANED_DIR = BASE_DIR / "data" / "cleaned"

OUTPUT_PATH = CLEANED_DIR / "cleaned_hr.csv"


# ============================================
# 2. LOAD DATASET
# ============================================

if not RAW_PATH.exists():
    raise FileNotFoundError(f"Dataset not found: {RAW_PATH}")

df = pd.read_csv(RAW_PATH)

print("\n========== DATASET LOADED ==========")

print("Original Rows:", df.shape[0])
print("Original Columns:", df.shape[1])


# ============================================
# 3. CLEAN COLUMN NAMES
# ============================================

df.columns = (
    df.columns
    .str.strip()
    .str.replace(" ", "_")
)

print("\n========== CLEANED COLUMN NAMES ==========")

print(df.columns.tolist())


# ============================================
# 4. REMOVE EXTRA SPACES
# ============================================

text_columns = df.select_dtypes(
    include=["object"]
).columns

for column in text_columns:

    df[column] = df[column].str.strip()

print("\n========== TEXT CLEANING COMPLETED ==========")


# ============================================
# 5. CHECK MISSING VALUES
# ============================================

print("\n========== MISSING VALUES BEFORE CLEANING ==========")

print(df.isnull().sum())

total_missing = df.isnull().sum().sum()

print("Total Missing Values:", total_missing)


# ============================================
# 6. HANDLE MISSING VALUES
# ============================================

numeric_columns = df.select_dtypes(
    include=["number"]
).columns

categorical_columns = df.select_dtypes(
    include=["object"]
).columns

# Fill numerical missing values with median
for column in numeric_columns:

    if df[column].isnull().sum() > 0:

        df[column] = df[column].fillna(
            df[column].median()
        )

# Fill categorical missing values with mode
for column in categorical_columns:

    if df[column].isnull().sum() > 0:

        mode_value = df[column].mode()

        if not mode_value.empty:

            df[column] = df[column].fillna(
                mode_value[0]
            )

print("\n========== MISSING VALUES HANDLED ==========")

print(df.isnull().sum().sum())


# ============================================
# 7. REMOVE DUPLICATES
# ============================================

duplicates = df.duplicated().sum()

print("\n========== DUPLICATE RECORDS ==========")

print("Duplicates Found:", duplicates)

df = df.drop_duplicates()

print("Duplicates Remaining:", df.duplicated().sum())


# ============================================
# 8. CHECK EMPLOYEE ID DUPLICATES
# ============================================

if "EmployeeNumber" in df.columns:

    employee_duplicates = df[
        "EmployeeNumber"
    ].duplicated().sum()

    print("\n========== EMPLOYEE ID CHECK ==========")

    print("Duplicate Employee Numbers:", employee_duplicates)

    if employee_duplicates > 0:

        raise ValueError(
            "Duplicate EmployeeNumber values found. "
            "Review these records before continuing."
        )


# ============================================
# 9. REMOVE UNNECESSARY COLUMNS
# ============================================

unnecessary_columns = [
    "EmployeeCount",
    "Over18",
    "StandardHours"
]

removed_columns = []

for column in unnecessary_columns:

    if column in df.columns and df[column].nunique(dropna=False) <= 1:

        df.drop(columns=[column], inplace=True)

        removed_columns.append(column)

print("\n========== UNNECESSARY COLUMNS ==========")

print("Removed Columns:", removed_columns)


# ============================================
# 10. CORRECT NUMERICAL DATA TYPES
# ============================================

numeric_fields = [
    "Age",
    "DailyRate",
    "DistanceFromHome",
    "Education",
    "EmployeeNumber",
    "EnvironmentSatisfaction",
    "HourlyRate",
    "JobInvolvement",
    "JobLevel",
    "JobSatisfaction",
    "MonthlyIncome",
    "MonthlyRate",
    "NumCompaniesWorked",
    "PercentSalaryHike",
    "PerformanceRating",
    "RelationshipSatisfaction",
    "StockOptionLevel",
    "TotalWorkingYears",
    "TrainingTimesLastYear",
    "WorkLifeBalance",
    "YearsAtCompany",
    "YearsInCurrentRole",
    "YearsSinceLastPromotion",
    "YearsWithCurrManager"
]

for column in numeric_fields:

    if column in df.columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )


# ============================================
# 11. VALIDATE ATTRITION VALUES
# ============================================

if "Attrition" in df.columns:

    print("\n========== ATTRITION VALIDATION ==========")

    print(df["Attrition"].value_counts())

    invalid_values = set(
        df["Attrition"].dropna().unique()
    ) - {"Yes", "No"}

    if invalid_values:

        raise ValueError(
            f"Unexpected Attrition values: {invalid_values}"
        )


# ============================================
# 12. FINAL MISSING VALUE CHECK
# ============================================

print("\n========== FINAL MISSING VALUES ==========")

print(df.isnull().sum())

if df.isnull().sum().sum() > 0:

    raise ValueError(
        "Missing values remain. Review the dataset before saving."
    )


# ============================================
# 13. FINAL DATASET INFORMATION
# ============================================

print("\n========== FINAL DATASET INFORMATION ==========")

print("Total Rows:", df.shape[0])

print("Total Columns:", df.shape[1])

print("Duplicate Records:", df.duplicated().sum())

print("Missing Values:", df.isnull().sum().sum())


# ============================================
# 14. SAVE CLEANED DATASET
# ============================================

CLEANED_DIR.mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    OUTPUT_PATH,
    index=False
)

print("\n========== DATA CLEANING COMPLETED ==========")

print("Cleaned Dataset Saved Successfully!")

print("File Location:", OUTPUT_PATH)
