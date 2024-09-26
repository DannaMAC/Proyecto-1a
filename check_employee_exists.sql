create or replace FUNCTION check_employee_exists (
    emp_no NUMBER) RETURN NUMBER
IS
    no_cont NUMBER;
    error_emp_not_found EXCEPTION;
BEGIN
    SELECT COUNT(*)
    INTO no_cont
    FROM EMP
    WHERE EMPNO = emp_no;

    IF no_cont = 0 THEN
        RAISE error_emp_not_found;
    ELSE
        RETURN 1;
    END IF;

    COMMIT;

EXCEPTION
    WHEN error_emp_not_found THEN
        RAISE_APPLICATION_ERROR(-20106, 'El empleado no existe');

    WHEN OTHERS THEN
        ROLLBACK;
        RAISE_APPLICATION_ERROR(-20006, 'Error desconocido en la verificacion de existencia del empleado');
END;