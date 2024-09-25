SET SERVEROUTPUT ON;

CREATE OR REPLACE FUNCTION noEmp_depto (
    no_dept NUMBER)
RETURN NUMBER
IS
    no_emp NUMBER;
    error_dept_has_no_emp EXCEPTION;
BEGIN
    SELECT COUNT(*) INTO no_emp FROM EMP WHERE deptno = no_dept;
    COMMIT;
    IF no_emp = 0 THEN
        RAISE error_dept_has_no_emp
    END IF;
    RETURN no_emp
EXCEPTION
    WHEN error_dept_has_no_emp THEN
        RAISE_APPLICATION_ERROR(-20107, 'El departamento no tiene empleados asociados.');

    WHEN OTHERS THEN
        ROLLBACK;
        RAISE_APPLICATION_ERROR(-20007, 'Error desconocido en la operación de eliminación del departamento.');
END;
/
