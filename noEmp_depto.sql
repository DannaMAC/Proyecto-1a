SET SERVEROUTPUT ON;

CREATE OR REPLACE PROCEDURE noEmp_depto (
    no_dept NUMBER)
IS
    no_emp NUMBER;
    error_dept_has_emp EXCEPTION;
BEGIN
    SELECT COUNT(*)
    INTO no_emp
    FROM EMP
    WHERE DEPTNO = no_dept;

    IF no_emp > 0 THEN
        RAISE error_dept_has_emp;
    END IF;

    DELETE FROM DEPT
    WHERE DEPTNO = no_dept;

    COMMIT;

EXCEPTION
    WHEN error_dept_has_emp THEN
        RAISE_APPLICATION_ERROR(-20107, 'No se puede eliminar el departamento porque tiene empleados asociados.');

    WHEN OTHERS THEN
        ROLLBACK;
        RAISE_APPLICATION_ERROR(-20007, 'Error desconocido en la operación de eliminación del departamento.');
END;
/
