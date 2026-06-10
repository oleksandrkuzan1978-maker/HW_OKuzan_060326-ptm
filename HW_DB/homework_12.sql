USE 060326_ptm_KUZAN;
/* Работайте со своей ранее созданной БД */


/* 1. Создайте хранимую процедуру get_department_id, которая
    принимает id сотрудника (IN-параметр), и возвращает id департамента
    (где работает сотрудник) через OUT-параметр. */
    
SELECT * from employees;

DELIMITER //
CREATE PROCEDURE get_department_id(IN id_emp INT, OUT id_dep INT)
BEGIN
SELECT department_id INTO id_dep FROM employees
WHERE id_emp = employee_id;
END //
DELIMITER ;
CALL get_department_id(116, @id_dep);
SELECT @id_dep AS dep_id;

/* 2. Создайте хранимую процедуру get_employee_age, которая
   принимает id сотрудника (IN-параметр)
   и возвращает его возраст через OUT-параметр. */

DELIMITER //
CREATE PROCEDURE get_employee_age(IN id_emp INT, OUT age_emp INT)
BEGIN
SELECT age INTO age_emp FROM employees
WHERE id_emp = employee_id;
END //
DELIMITER ;

CALL get_employee_age(111, @age_emp);
SELECT @age_emp AS age_employee;

/* 3. Создайте хранимую процедуру increase_salary, которая
   принимает зарплату сотрудника (INOUT-параметр) и уменьшает ее на 10%. */

DROP PROCEDURE IF EXISTS decrease_salary; 

DELIMITER //
CREATE PROCEDURE decrease_salary(INOUT sal FLOAT)
BEGIN
SET sal = sal * 0.9;
END //
DELIMITER ;

SET @sal = 4500;
CALL decrease_salary(@sal);
SELECT ROUND(@sal, 2) AS decreased_salary;
   
   