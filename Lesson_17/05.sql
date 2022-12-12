SELECT
  first_name,
  last_name,
  job_id,
  department_id
FROM
  pds.employees
  JOIN pds.departments USING (department_id)
  JOIN pds.locations USING (location_id)
WHERE
  city = 'London';