create or replace FUNCTION check_department_exists (
    deptnod NUMBER) RETURN NUMBER
IS
    no_cont NUMBER;
    error_dept_not_found EXCEPTION;
BEGIN
    SELECT COUNT(*)
    INTO no_cont
    FROM DEPT
    WHERE DEPTNO = deptnod;

    IF no_cont = 0 THEN
        RAISE error_dept_not_found;
    ELSE
        RETURN 1;
    END IF;

    COMMIT;

EXCEPTION
    WHEN error_dept_not_found THEN
        RAISE_APPLICATION_ERROR(-20106, 'El departamento no existe');

    WHEN OTHERS THEN
        ROLLBACK;
        RAISE_APPLICATION_ERROR(-20006, 'Error desconocido en la verificacion de existencia del departamento');
END;