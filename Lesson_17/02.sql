SELECT 
	AVG(SALARY) AS MEAN_SALARY,
    COUNT(EMPLOYEE_ID) AS COUNT_EMPLOYEE
FROM
	pds.employees
WHERE
	DEPARTMENT_ID = 90;