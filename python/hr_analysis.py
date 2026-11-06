
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path

# ============================================
# 1. PROJECT PATHS
# ============================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "cleaned" / "cleaned_hr.csv"

CHART_DIR = BASE_DIR / "outputs" / "charts"

REPORT_DIR = BASE_DIR / "outputs" / "reports"

CHART_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================
# 2. LOAD DATASET
# ============================================

if not DATA_PATH.exists():
    raise FileNotFoundError(
        f"Cleaned dataset not found: {DATA_PATH}"
    )

df = pd.read_csv(DATA_PATH)

print("\n========== HR DATASET LOADED ==========")

print("Total Employees:", len(df))
print("Total Columns:", len(df.columns))


# ============================================
# 3. GENERAL HR STATISTICS
# ============================================

total_employees = len(df)

employees_left = (
    df["Attrition"] == "Yes"
).sum()

employees_stayed = (
    df["Attrition"] == "No"
).sum()

attrition_rate = (
    employees_left / total_employees
) * 100

retention_rate = (
    employees_stayed / total_employees
) * 100

average_age = df["Age"].mean()

average_income = df["MonthlyIncome"].mean()

average_years = df["TotalWorkingYears"].mean()

print("\n========== HR KEY PERFORMANCE INDICATORS ==========")

print("Total Employees:", total_employees)

print("Employees Left:", employees_left)

print("Employees Stayed:", employees_stayed)

print("Attrition Rate:", round(attrition_rate, 2), "%")

print("Retention Rate:", round(retention_rate, 2), "%")

print("Average Age:", round(average_age, 2))

print("Average Monthly Income:", round(average_income, 2))

print("Average Working Experience:", round(average_years, 2))


# ============================================
# 4. SAVE KPI REPORT
# ============================================

kpi_data = {
    "Metric": [
        "Total Employees",
        "Employees Left",
        "Employees Stayed",
        "Attrition Rate",
        "Retention Rate",
        "Average Age",
        "Average Monthly Income",
        "Average Working Experience"
    ],

    "Value": [
        total_employees,
        employees_left,
        employees_stayed,
        round(attrition_rate, 2),
        round(retention_rate, 2),
        round(average_age, 2),
        round(average_income, 2),
        round(average_years, 2)
    ]
}

kpi_df = pd.DataFrame(kpi_data)

kpi_df.to_csv(
    REPORT_DIR / "hr_kpis.csv",
    index=False
)


# ============================================
# 5. ATTRITION DISTRIBUTION
# ============================================

print("\n========== ATTRITION DISTRIBUTION ==========")

print(df["Attrition"].value_counts())

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Attrition"
)

plt.title("Employee Attrition Distribution")

plt.xlabel("Attrition")

plt.ylabel("Number of Employees")

plt.tight_layout()

plt.savefig(
    CHART_DIR / "attrition_distribution.png",
    dpi=300
)

plt.close()


# ============================================
# 6. DEPARTMENT-WISE ATTRITION
# ============================================

print("\n========== DEPARTMENT-WISE ATTRITION ==========")

department_analysis = df.groupby(
    "Department"
).agg(
    Total_Employees=("Attrition", "size"),
    Employees_Left=(
        "Attrition",
        lambda x: (x == "Yes").sum()
    )
)

department_analysis["Attrition_Rate"] = (
    department_analysis["Employees_Left"] /
    department_analysis["Total_Employees"]
) * 100

print(department_analysis)

department_analysis.to_csv(
    REPORT_DIR / "department_analysis.csv"
)

plt.figure(figsize=(10, 6))

sns.barplot(
    data=department_analysis.reset_index(),
    x="Department",
    y="Attrition_Rate"
)

plt.title("Department-wise Attrition Rate")

plt.xlabel("Department")

plt.ylabel("Attrition Rate (%)")

plt.tight_layout()

plt.savefig(
    CHART_DIR / "department_attrition.png",
    dpi=300
)

plt.close()


# ============================================
# 7. GENDER-WISE ATTRITION
# ============================================

print("\n========== GENDER-WISE ATTRITION ==========")

gender_analysis = df.groupby(
    "Gender"
).agg(
    Total_Employees=("Attrition", "size"),
    Employees_Left=(
        "Attrition",
        lambda x: (x == "Yes").sum()
    )
)

gender_analysis["Attrition_Rate"] = (
    gender_analysis["Employees_Left"] /
    gender_analysis["Total_Employees"]
) * 100

print(gender_analysis)

gender_analysis.to_csv(
    REPORT_DIR / "gender_analysis.csv"
)


# ============================================
# 8. AGE-WISE ATTRITION
# ============================================

print("\n========== AGE-WISE ATTRITION ==========")

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[17, 25, 35, 45, 55, 100],
    labels=[
        "18-24",
        "25-34",
        "35-44",
        "45-54",
        "55+"
    ]
)

age_analysis = df.groupby(
    "Age_Group",
    observed=False
).agg(
    Total_Employees=("Attrition", "size"),
    Employees_Left=(
        "Attrition",
        lambda x: (x == "Yes").sum()
    )
)

age_analysis["Attrition_Rate"] = (
    age_analysis["Employees_Left"] /
    age_analysis["Total_Employees"].replace(0, np.nan)
) * 100

print(age_analysis)

age_analysis.to_csv(
    REPORT_DIR / "age_analysis.csv"
)

plt.figure(figsize=(10, 6))

sns.countplot(
    data=df,
    x="Age_Group",
    hue="Attrition"
)

plt.title("Age Group-wise Employee Attrition")

plt.xlabel("Age Group")

plt.ylabel("Number of Employees")

plt.tight_layout()

plt.savefig(
    CHART_DIR / "age_attrition.png",
    dpi=300
)

plt.close()


# ============================================
# 9. SALARY ANALYSIS
# ============================================

print("\n========== SALARY ANALYSIS ==========")

salary_analysis = df.groupby(
    "Attrition"
)["MonthlyIncome"].agg(
    ["mean", "median", "min", "max"]
)

print(salary_analysis)

salary_analysis.to_csv(
    REPORT_DIR / "salary_analysis.csv"
)

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df,
    x="Attrition",
    y="MonthlyIncome"
)

plt.title("Monthly Income vs Employee Attrition")

plt.xlabel("Attrition")

plt.ylabel("Monthly Income")

plt.tight_layout()

plt.savefig(
    CHART_DIR / "salary_attrition.png",
    dpi=300
)

plt.close()


# ============================================
# 10. OVERTIME ANALYSIS
# ============================================

print("\n========== OVERTIME ANALYSIS ==========")

overtime_analysis = df.groupby(
    "OverTime"
).agg(
    Total_Employees=("Attrition", "size"),
    Employees_Left=(
        "Attrition",
        lambda x: (x == "Yes").sum()
    )
)

overtime_analysis["Attrition_Rate"] = (
    overtime_analysis["Employees_Left"] /
    overtime_analysis["Total_Employees"]
) * 100

print(overtime_analysis)

overtime_analysis.to_csv(
    REPORT_DIR / "overtime_analysis.csv"
)

plt.figure(figsize=(8, 5))

sns.barplot(
    data=overtime_analysis.reset_index(),
    x="OverTime",
    y="Attrition_Rate"
)

plt.title("Overtime vs Attrition Rate")

plt.xlabel("Overtime")

plt.ylabel("Attrition Rate (%)")

plt.tight_layout()

plt.savefig(
    CHART_DIR / "overtime_attrition.png",
    dpi=300
)

plt.close()


# ============================================
# 11. JOB ROLE ANALYSIS
# ============================================

print("\n========== JOB ROLE ANALYSIS ==========")

jobrole_analysis = df.groupby(
    "JobRole"
).agg(
    Total_Employees=("Attrition", "size"),
    Employees_Left=(
        "Attrition",
        lambda x: (x == "Yes").sum()
    )
)

jobrole_analysis["Attrition_Rate"] = (
    jobrole_analysis["Employees_Left"] /
    jobrole_analysis["Total_Employees"]
) * 100

jobrole_analysis = jobrole_analysis.sort_values(
    "Attrition_Rate",
    ascending=False
)

print(jobrole_analysis)

jobrole_analysis.to_csv(
    REPORT_DIR / "jobrole_analysis.csv"
)

plt.figure(figsize=(12, 7))

sns.barplot(
    data=jobrole_analysis.reset_index(),
    x="Attrition_Rate",
    y="JobRole"
)

plt.title("Job Role-wise Attrition Rate")

plt.xlabel("Attrition Rate (%)")

plt.ylabel("Job Role")

plt.tight_layout()

plt.savefig(
    CHART_DIR / "jobrole_attrition.png",
    dpi=300
)

plt.close()


# ============================================
# 12. JOB SATISFACTION ANALYSIS
# ============================================

print("\n========== JOB SATISFACTION ANALYSIS ==========")

satisfaction_analysis = df.groupby(
    "JobSatisfaction"
).agg(
    Total_Employees=("Attrition", "size"),
    Employees_Left=(
        "Attrition",
        lambda x: (x == "Yes").sum()
    )
)

satisfaction_analysis["Attrition_Rate"] = (
    satisfaction_analysis["Employees_Left"] /
    satisfaction_analysis["Total_Employees"]
) * 100

print(satisfaction_analysis)

satisfaction_analysis.to_csv(
    REPORT_DIR / "satisfaction_analysis.csv"
)


# ============================================
# 13. EXPERIENCE ANALYSIS
# ============================================

print("\n========== EXPERIENCE ANALYSIS ==========")

experience_analysis = df.groupby(
    "Attrition"
).agg(
    Average_Total_Experience=("TotalWorkingYears", "mean"),
    Average_Company_Years=("YearsAtCompany", "mean"),
    Average_Current_Role_Years=("YearsInCurrentRole", "mean"),
    Average_Years_Since_Promotion=("YearsSinceLastPromotion", "mean")
)

print(experience_analysis)

experience_analysis.to_csv(
    REPORT_DIR / "experience_analysis.csv"
)


# ============================================
# 14. WORK-LIFE BALANCE ANALYSIS
# ============================================

print("\n========== WORK-LIFE BALANCE ANALYSIS ==========")

worklife_analysis = df.groupby(
    "WorkLifeBalance"
).agg(
    Total_Employees=("Attrition", "size"),
    Employees_Left=(
        "Attrition",
        lambda x: (x == "Yes").sum()
    )
)

worklife_analysis["Attrition_Rate"] = (
    worklife_analysis["Employees_Left"] /
    worklife_analysis["Total_Employees"]
) * 100

print(worklife_analysis)

worklife_analysis.to_csv(
    REPORT_DIR / "worklife_analysis.csv"
)


# ============================================
# 15. CORRELATION ANALYSIS
# ============================================

print("\n========== CORRELATION ANALYSIS ==========")

numeric_df = df.select_dtypes(
    include=["number"]
).copy()

numeric_df["Attrition_Flag"] = (
    df["Attrition"] == "Yes"
).astype(int)

correlation = numeric_df.corr()

print(
    correlation["Attrition_Flag"]
    .sort_values(ascending=False)
)

correlation.to_csv(
    REPORT_DIR / "correlation_analysis.csv"
)

plt.figure(figsize=(16, 12))

sns.heatmap(
    correlation,
    cmap="coolwarm",
    center=0,
    linewidths=0.3
)

plt.title("HR Employee Correlation Heatmap")

plt.tight_layout()

plt.savefig(
    CHART_DIR / "correlation_heatmap.png",
    dpi=300
)

plt.close()


# ============================================
# 16. ATTRITION BY DEPARTMENT AND GENDER
# ============================================

print("\n========== DEPARTMENT AND GENDER ANALYSIS ==========")

department_gender = df.pivot_table(
    index="Department",
    columns="Gender",
    values="EmployeeNumber",
    aggfunc="count"
)

print(department_gender)

department_gender.to_csv(
    REPORT_DIR / "department_gender_analysis.csv"
)


# ============================================
# 17. BUSINESS INSIGHTS
# ============================================

print("\n========== BUSINESS INSIGHTS ==========")

highest_department = department_analysis[
    "Attrition_Rate"
].idxmax()

highest_jobrole = jobrole_analysis[
    "Attrition_Rate"
].idxmax()

highest_overtime = overtime_analysis[
    "Attrition_Rate"
].idxmax()

print(
    "Overall Attrition Rate:",
    round(attrition_rate, 2), "%"
)

print(
    "Department with Highest Attrition:",
    highest_department
)

print(
    "Job Role with Highest Attrition:",
    highest_jobrole
)

print(
    "Overtime Group with Highest Attrition:",
    highest_overtime
)


# ============================================
# 18. FINAL STATUS
# ============================================

print("\n========== HR ANALYSIS COMPLETED ==========")

print("Charts saved in:", CHART_DIR)

print("Reports saved in:", REPORT_DIR)
