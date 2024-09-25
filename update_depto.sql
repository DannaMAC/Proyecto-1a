SET SERVEROUTPUT ON;

CREATE OR REPLACE PROCEDURE update_depto (
    no_dept NUMBER,
    field VARCHAR2,
    new_v VARCHAR2)
IS
    no_cont NUMBER;
    OpSql VARCHAR2(400);
    error_dept_not_found EXCEPTION;
BEGIN
    SELECT COUNT(*)
    INTO no_cont
    FROM DEPT
    WHERE DEPTNO = no_dept;

    IF no_cont = 0 THEN
        RAISE error_dept_not_found;
    END IF;

    OpSql := 'UPDATE DEPT SET '||field||' = :d_new WHERE deptno = :dep_id';
    EXECUTE IMMEDIATE OpSql USING new_v, no_dept;

    COMMIT;

EXCEPTION
    WHEN error_dept_not_found THEN
        RAISE_APPLICATION_ERROR(-20103, 'El departamento no existe');
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE_APPLICATION_ERROR(-20002, 'Error desconocido en la actualización del departamento');
END;
/
