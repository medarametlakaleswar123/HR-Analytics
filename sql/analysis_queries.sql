
USE hr_analytics;

-- =====================================================
-- 1. OVERALL EMPLOYEE ATTRITION KPI
-- =====================================================

SELECT
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    SUM(CASE WHEN Attrition = 'No' THEN 1 ELSE 0 END) AS Employees_Stayed,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate,
    ROUND(
        SUM(CASE WHEN Attrition = 'No' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Retention_Rate
FROM hr_employee;


-- =====================================================
-- 2. DEPARTMENT-WISE ATTRITION
-- =====================================================

SELECT
    Department,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate
FROM hr_employee
GROUP BY Department
ORDER BY Attrition_Rate DESC;


-- =====================================================
-- 3. GENDER-WISE ATTRITION
-- =====================================================

SELECT
    Gender,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate
FROM hr_employee
GROUP BY Gender;


-- =====================================================
-- 4. AGE GROUP-WISE ATTRITION
-- =====================================================

SELECT
    CASE
        WHEN Age BETWEEN 18 AND 24 THEN '18-24'
        WHEN Age BETWEEN 25 AND 34 THEN '25-34'
        WHEN Age BETWEEN 35 AND 44 THEN '35-44'
        WHEN Age BETWEEN 45 AND 54 THEN '45-54'
        ELSE '55+'
    END AS Age_Group,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate
FROM hr_employee
GROUP BY Age_Group
ORDER BY MIN(Age);


-- =====================================================
-- 5. SALARY-WISE ATTRITION
-- =====================================================

SELECT
    CASE
        WHEN MonthlyIncome < 3000 THEN 'Below 3000'
        WHEN MonthlyIncome BETWEEN 3000 AND 4999 THEN '3000-4999'
        WHEN MonthlyIncome BETWEEN 5000 AND 7999 THEN '5000-7999'
        ELSE '8000+'
    END AS Salary_Band,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate
FROM hr_employee
GROUP BY Salary_Band
ORDER BY MIN(MonthlyIncome);


-- =====================================================
-- 6. OVERTIME-WISE ATTRITION
-- =====================================================

SELECT
    OverTime,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate
FROM hr_employee
GROUP BY OverTime;


-- =====================================================
-- 7. JOB ROLE-WISE ATTRITION
-- =====================================================

SELECT
    JobRole,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate
FROM hr_employee
GROUP BY JobRole
ORDER BY Attrition_Rate DESC;


-- =====================================================
-- 8. JOB SATISFACTION VS ATTRITION
-- =====================================================

SELECT
    JobSatisfaction,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate
FROM hr_employee
GROUP BY JobSatisfaction
ORDER BY JobSatisfaction;


-- =====================================================
-- 9. WORK-LIFE BALANCE VS ATTRITION
-- =====================================================

SELECT
    WorkLifeBalance,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate
FROM hr_employee
GROUP BY WorkLifeBalance
ORDER BY WorkLifeBalance;


-- =====================================================
-- 10. EMPLOYEE METRICS: LEFT VS STAYED
-- =====================================================

SELECT
    Attrition,
    COUNT(*) AS Total_Employees,
    ROUND(AVG(Age), 2) AS Average_Age,
    ROUND(AVG(MonthlyIncome), 2) AS Average_Monthly_Income,
    ROUND(AVG(YearsAtCompany), 2) AS Average_Years_At_Company,
    ROUND(AVG(YearsSinceLastPromotion), 2) AS Average_Years_Since_Promotion,
    ROUND(AVG(JobSatisfaction), 2) AS Average_Job_Satisfaction
FROM hr_employee
GROUP BY Attrition;


-- =====================================================
-- 11. BUSINESS TRAVEL VS ATTRITION
-- =====================================================

SELECT
    BusinessTravel,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate
FROM hr_employee
GROUP BY BusinessTravel
ORDER BY Attrition_Rate DESC;


-- =====================================================
-- 12. DEPARTMENT AND JOB ROLE ANALYSIS
-- =====================================================

SELECT
    Department,
    JobRole,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate
FROM hr_employee
GROUP BY Department, JobRole
ORDER BY Department, Attrition_Rate DESC;


-- =====================================================
-- 13. DEPARTMENT RANKING USING DENSE_RANK
-- =====================================================

WITH Department_Analysis AS (
    SELECT
        Department,
        COUNT(*) AS Total_Employees,
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
        ROUND(
            SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
            * 100.0 / COUNT(*), 2
        ) AS Attrition_Rate
    FROM hr_employee
    GROUP BY Department
)
SELECT
    Department,
    Total_Employees,
    Employees_Left,
    Attrition_Rate,
    DENSE_RANK() OVER (ORDER BY Attrition_Rate DESC) AS Department_Rank
FROM Department_Analysis;


-- =====================================================
-- 14. JOB ROLE RANKING USING WINDOW FUNCTION
-- =====================================================

SELECT
    JobRole,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate,
    DENSE_RANK() OVER (
        ORDER BY
            SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
            * 100.0 / COUNT(*) DESC
    ) AS JobRole_Rank
FROM hr_employee
GROUP BY JobRole;


-- =====================================================
-- 15. LONG TENURE EMPLOYEES WITH NO RECENT PROMOTION
-- =====================================================

SELECT
    EmployeeNumber,
    Age,
    Department,
    JobRole,
    MonthlyIncome,
    YearsAtCompany,
    YearsSinceLastPromotion,
    Attrition
FROM hr_employee
WHERE YearsAtCompany >= 5
  AND YearsSinceLastPromotion >= 3
ORDER BY YearsSinceLastPromotion DESC;


-- =====================================================
-- 16. EDUCATION FIELD-WISE ATTRITION
-- =====================================================

SELECT
    EducationField,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate
FROM hr_employee
GROUP BY EducationField
ORDER BY Attrition_Rate DESC;
