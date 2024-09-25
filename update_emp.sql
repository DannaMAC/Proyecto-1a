SET SERVEROUTPUT ON;

CREATE OR REPLACE PROCEDURE update_emp (
    emp_no NUMBER,
    e_name VARCHAR2,
    e_job VARCHAR2,
    e_mgr NUMBER,
    e_hiredate DATE,
    e_sal NUMBER,
    e_comm NUMBER,
    e_deptno NUMBER)
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
    END IF;

    UPDATE EMP
    SET ENAME = e_name,
        JOB = e_job,
        MGR = e_mgr,
        HIREDATE = e_hiredate,
        SAL = e_sal,
        COMM = e_comm,
        DEPTNO = e_deptno
    WHERE EMPNO = emp_no;

    COMMIT;

EXCEPTION
    WHEN error_emp_not_found THEN
        RAISE_APPLICATION_ERROR(-20105, 'El empleado no existe');

    WHEN OTHERS THEN
        ROLLBACK;
        RAISE_APPLICATION_ERROR(-20005, 'Error desconocido en la actualización del empleado');
END;
/
