# HR Analytics – Employee Attrition Analysis | Data Analytics Project

## Project Overview

HR Analytics – Employee Attrition Analysis is an end-to-end Data Analytics project using the IBM HR Analytics Employee Attrition & Performance dataset.

The main objective is to analyze employee data, identify employee turnover patterns, understand factors associated with attrition, and generate meaningful HR insights to support better workforce management and employee retention strategies.

This project uses Python for data cleaning and exploratory data analysis, MySQL for SQL-based business analysis, and Power BI for interactive dashboard development.

## Project Objectives

- Analyze overall employee attrition and retention rates.
- Identify departments with higher employee turnover.
- Understand employee attrition based on age and gender.
- Analyze salary differences between employees who leave and stay.
- Evaluate the relationship between overtime and employee attrition.
- Analyze job satisfaction and work-life balance.
- Identify job roles with higher attrition rates.
- Understand employee experience and promotion patterns.
- Build interactive dashboards to communicate HR insights.

## Technologies and Tools

| Technology | Purpose |
|---|---|
| Python | Data cleaning and analysis |
| Pandas | Data manipulation and preprocessing |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical data visualization |
| MySQL | Database management |
| SQL | Business data analysis |
| Power BI | Interactive dashboard development |
| Excel | Spreadsheet analysis |
| VS Code | Development environment |
| Git & GitHub | Version control |

## Dataset Information

**Dataset:** IBM HR Analytics Employee Attrition & Performance

The dataset contains employee information, including:

- Employee Number
- Age
- Gender
- Department
- Education and Education Field
- Job Role
- Job Level
- Monthly Income
- Daily Rate
- Hourly Rate
- OverTime
- Job Satisfaction
- Environment Satisfaction
- Relationship Satisfaction
- Work-Life Balance
- Years at Company
- Years in Current Role
- Years Since Last Promotion
- Total Working Years
- Attrition

**Dataset Summary**

| Description | Details |
|---|---:|
| Total Employees | 1,470 |
| Original Columns | 35 |
| Cleaned Columns | 32 |
| Target Variable | Attrition |
| Attrition Categories | Yes / No |

## Project Workflow

### 1. Data Cleaning Using Python

Used Pandas to clean and prepare the raw HR dataset.

**File:** `python/data_cleaning.py`

Tasks performed:

- Loaded the raw CSV dataset.
- Inspected dataset structure, columns, and data types.
- Checked missing values and duplicate records.
- Removed duplicate records.
- Cleaned column names and text values.
- Handled missing values.
- Removed constant columns.
- Validated employee records.
- Exported the cleaned dataset.

**Output:** `data/cleaned/cleaned_hr.csv`

### 2. Exploratory Data Analysis (EDA)

Performed exploratory data analysis using Pandas, NumPy, Matplotlib, and Seaborn.

**File:** `python/hr_analysis.py`

Analysis performed:

- Total Employees and Employees Left.
- Overall Attrition and Retention Rates.
- Department-wise Attrition.
- Gender-wise Attrition.
- Age-group Attrition.
- Salary Analysis.
- Overtime vs. Attrition.
- Job Role-wise Attrition.
- Job Satisfaction Analysis.
- Work-Life Balance Analysis.
- Employee Experience Analysis.
- Correlation Analysis.

Generated charts and analytical reports to identify employee turnover patterns and workforce trends.

### 3. SQL Analysis Using MySQL

Imported the cleaned dataset into MySQL and performed business analysis using SQL.

**Files:**
- `sql/database.sql`
- `sql/analysis_queries.sql`
- `python/import_to_mysql.py`

Created database:

`hr_analytics`

Created table:

`hr_employee`

SQL concepts used:

- SELECT, DISTINCT, WHERE
- AND, OR, BETWEEN, IN
- ORDER BY and LIMIT
- Aggregate Functions
- GROUP BY and HAVING
- CASE Statements
- Subqueries
- Common Table Expressions (CTEs)
- Window Functions
- RANK(), DENSE_RANK(), ROW_NUMBER()
- Conditional Aggregation
- Attrition Rate Calculations
- Department and Job Role Analysis

SQL scripts are available in the `sql/` directory.

### 4. Power BI Dashboard Development

Developing an interactive HR Analytics dashboard using Power BI.

**File:** `powerbi/HR-Analytics.pbix`

Dashboard components:

**Page 1: HR Overview**

- Total Employees
- Employees Left
- Employees Stayed
- Attrition Rate
- Department-wise Attrition
- Overall Employee Attrition

**Page 2: Employee Demographics**

- Age-group Analysis
- Gender-wise Attrition
- Education Field Analysis
- Marital Status Analysis

**Page 3: Department & Job Role Analysis**

- Department-wise Attrition
- Job Role-wise Attrition
- Job Level Analysis
- Monthly Income Analysis

**Page 4: Employee Satisfaction & Retention**

- Job Satisfaction
- Work-Life Balance
- Overtime Analysis
- Years at Company
- Years Since Last Promotion

Interactive Dashboard Features:

- Department slicer
- Gender slicer
- Job Role slicer
- Age-group analysis
- Interactive filtering
- Employee attrition analysis

## Project Folder Structure

```text
HR-Analytics/
│
├── data/
│   ├── raw/
│   │   └── HR-Employee-Attrition.csv
│   │
│   └── cleaned/
│       └── cleaned_hr.csv
│
├── excel/
│
├── notebooks/
│
├── outputs/
│   ├── charts/
│   │   ├── age_attrition.png
│   │   ├── attrition_distribution.png
│   │   ├── correlation_heatmap.png
│   │   ├── department_attrition.png
│   │   ├── jobrole_attrition.png
│   │   ├── overtime_attrition.png
│   │   └── salary_attrition.png
│   │
│   └── reports/
│       ├── age_analysis.csv
│       ├── correlation_analysis.csv
│       ├── department_analysis.csv
│       ├── department_gender_analysis.csv
│       ├── experience_analysis.csv
│       ├── gender_analysis.csv
│       ├── hr_kpis.csv
│       ├── jobrole_analysis.csv
│       ├── overtime_analysis.csv
│       ├── salary_analysis.csv
│       ├── satisfaction_analysis.csv
│       └── worklife_analysis.csv
│
├── powerbi/
│   └── HR-Analytics.pbix
│
├── python/
│   ├── data_cleaning.py
│   ├── import_to_mysql.py
│   └── hr_analysis.py
│
├── sql/
│   ├── database.sql
│   └── analysis_queries.sql
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## How to Run the Project

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL

cd HR-Analytics
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root using `.env.example`.

Configure your local MySQL credentials:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=hr_analytics
```

Never upload your actual `.env` file to GitHub.

### 4. Run Data Cleaning

```bash
python python/data_cleaning.py
```

### 5. Run Exploratory Data Analysis

```bash
python python/hr_analysis.py
```

### 6. Create MySQL Database

Open `sql/database.sql` in MySQL Workbench and execute the SQL script.

### 7. Import Data into MySQL

Make sure MySQL is running and the database is configured.

```bash
python python/import_to_mysql.py
```

### 8. Execute SQL Queries

Open the SQL files from the `sql/` directory using MySQL Workbench and execute the queries.

### 9. Open the Power BI Dashboard

Open the following file using Power BI Desktop:

`powerbi/HR-Analytics.pbix`

## Key Business Insights

This project helps identify:

- Departments contributing to higher employee attrition.
- Employee age groups experiencing higher turnover.
- Differences in attrition between male and female employees.
- The relationship between monthly income and employee retention.
- The impact of overtime on employee attrition.
- Job roles experiencing higher employee turnover.
- Employee satisfaction and work-life balance patterns.
- The relationship between employee experience and attrition.

## Skills Demonstrated

- Data Collection and Loading
- Data Cleaning and Preprocessing
- Exploratory Data Analysis
- Data Manipulation
- Python Programming
- SQL Querying
- MySQL Database Management
- Business Analysis
- KPI Analysis
- Statistical Analysis
- Data Visualization
- Power BI Dashboard Development
- Business Insights Generation

## Power BI Dashboard Screenshots

### 1. HR Overview

HR Overview Dashboard

### 2. Employee Demographics

Employee Demographics Analysis

### 3. Department & Job Role Analysis

Department and Job Role Analysis

### 4. Employee Satisfaction & Retention

Employee Satisfaction and Retention Analysis

## Author

**Medarametla Kaleswararao**

Aspiring Data Analyst

**Technical Skills:** Python | SQL | MySQL | Pandas | NumPy | Matplotlib | Seaborn | Power BI | Excel

## About

End-to-end HR Analytics project using Python, SQL, MySQL, and Power BI to analyze employee attrition and generate meaningful workforce insights.