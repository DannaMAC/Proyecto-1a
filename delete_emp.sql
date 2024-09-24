SET SERVEROUTPUT ON;

CREATE OR REPLACE PROCEDURE delete_emp (
    empno NUMBER)
IS
    no_cont NUMBER;
    error_emp_not_found EXCEPTION;
BEGIN
    SELECT COUNT(*)
    INTO no_cont
    FROM EMP
    WHERE EMPNO = empno;

    IF no_cont = 0 THEN
        RAISE error_emp_not_found;
    END IF;

    DELETE FROM EMP
    WHERE EMPNO = empno;

    COMMIT;

EXCEPTION
    WHEN error_emp_not_found THEN
        RAISE_APPLICATION_ERROR(-20106, 'El empleado no existe');

    WHEN OTHERS THEN
        ROLLBACK;
        RAISE_APPLICATION_ERROR(-20006, 'Error desconocido en la eliminación del empleado');
END;
/
