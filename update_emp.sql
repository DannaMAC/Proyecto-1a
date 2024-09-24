SET SERVEROUTPUT ON;

CREATE OR REPLACE PROCEDURE update_emp (
    empno NUMBER,
    ename VARCHAR2,
    job VARCHAR2,
    mgr NUMBER,
    hiredate DATE,
    sal NUMBER,
    comm NUMBER,
    deptno NUMBER)
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

    UPDATE EMP
    SET ENAME = ename,
        JOB = job,
        MGR = mgr,
        HIREDATE = hiredate,
        SAL = sal,
        COMM = comm,
        DEPTNO = deptno
    WHERE EMPNO = empno;

    COMMIT;

EXCEPTION
    WHEN error_emp_not_found THEN
        RAISE_APPLICATION_ERROR(-20105, 'El empleado no existe');

    WHEN OTHERS THEN
        ROLLBACK;
        RAISE_APPLICATION_ERROR(-20005, 'Error desconocido en la actualización del empleado');
END;
/
