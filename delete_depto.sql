SET SERVEROUTPUT ON;

CREATE OR REPLACE PROCEDURE delete_depto (
    no_dept NUMBER)
IS
    no_cont NUMBER;
    error_dept_not_found EXCEPTION;
BEGIN

    SELECT COUNT(*)
    INTO no_cont
    FROM DEPT
    WHERE DEPTNO = no_dept;

    IF no_cont = 0 THEN
        RAISE error_dept_not_found;
    END IF;

    DELETE FROM DEPT
    WHERE DEPTNO = no_dept;

    COMMIT;

EXCEPTION
    WHEN error_dept_not_found THEN
        RAISE_APPLICATION_ERROR(-20103, 'El departamento no existe');

    WHEN OTHERS THEN
        ROLLBACK;
        RAISE_APPLICATION_ERROR(-20003, 'Error desconocido en la eliminación del departamento');
END;
/

