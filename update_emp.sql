SET SERVEROUTPUT ON;

CREATE OR REPLACE PROCEDURE update_emp (
    emp_no NUMBER,
    field VARCHAR2,
    new_v VARCHAR2)
IS
    no_cont NUMBER;
    OpSql VARCHAR2(400);
    error_emp_not_found EXCEPTION;
BEGIN
    SELECT COUNT(*)
    INTO no_cont
    FROM EMP
    WHERE EMPNO = emp_no;

    IF no_cont = 0 THEN
        RAISE error_emp_not_found;
    END IF;

    OpSql := 'UPDATE EMP SET '||field||' = :e_new WHERE empno = :emp_id';
    EXECUTE IMMEDIATE OpSql USING new_v, emp_no;

    COMMIT;

EXCEPTION
    WHEN error_emp_not_found THEN
        RAISE_APPLICATION_ERROR(-20105, 'El empleado no existe');

    WHEN OTHERS THEN
        ROLLBACK;
        RAISE_APPLICATION_ERROR(-20005, 'Error desconocido en la actualización del empleado');
END;
/