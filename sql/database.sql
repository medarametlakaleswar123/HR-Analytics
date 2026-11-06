
-- ============================================
-- HR ANALYTICS PROJECT
-- DATABASE CREATION
-- ============================================

-- 1. CREATE DATABASE

CREATE DATABASE IF NOT EXISTS hr_analytics;

-- 2. SELECT DATABASE

USE hr_analytics;


-- ============================================
-- 3. CREATE EMPLOYEE TABLE
-- ============================================

CREATE TABLE IF NOT EXISTS hr_employee (

    Age INT,

    Attrition VARCHAR(10),

    BusinessTravel VARCHAR(50),

    DailyRate INT,

    Department VARCHAR(100),

    DistanceFromHome INT,

    Education INT,

    EducationField VARCHAR(100),

    EmployeeNumber INT PRIMARY KEY,

    EnvironmentSatisfaction INT,

    Gender VARCHAR(20),

    HourlyRate INT,

    JobInvolvement INT,

    JobLevel INT,

    JobRole VARCHAR(100),

    JobSatisfaction INT,

    MaritalStatus VARCHAR(30),

    MonthlyIncome INT,

    MonthlyRate INT,

    NumCompaniesWorked INT,

    OverTime VARCHAR(10),

    PercentSalaryHike INT,

    PerformanceRating INT,

    RelationshipSatisfaction INT,

    StockOptionLevel INT,

    TotalWorkingYears INT,

    TrainingTimesLastYear INT,

    WorkLifeBalance INT,

    YearsAtCompany INT,

    YearsInCurrentRole INT,

    YearsSinceLastPromotion INT,

    YearsWithCurrManager INT

);


-- ============================================
-- 4. VERIFY DATABASE
-- ============================================

SHOW DATABASES;


-- ============================================
-- 5. VERIFY TABLES
-- ============================================

SHOW TABLES;


-- ============================================
-- 6. VERIFY TABLE STRUCTURE
-- ============================================

DESCRIBE hr_employee;


-- ============================================
-- 7. VERIFY TABLE RECORD COUNT
-- ============================================

SELECT COUNT(*) AS Total_Employees
FROM hr_employee;


-- ============================================
-- 8. VERIFY TABLE DATA
-- ============================================

SELECT *
FROM hr_employee
LIMIT 10;


-- ============================================
-- DATABASE CREATION COMPLETED
-- ============================================
