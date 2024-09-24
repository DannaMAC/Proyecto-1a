SET SERVEROUTPUT ON;

CREATE OR REPLACE PROCEDURE add_emp (
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
    error_emp_rep EXCEPTION;
BEGIN
    SELECT COUNT(*)
    INTO no_cont
    FROM EMP
    WHERE EMPNO = empno;

    IF no_cont > 0 THEN
        RAISE error_emp_rep;
    END IF;

    INSERT INTO EMP (EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO)
    VALUES (empno, ename, job, mgr, hiredate, sal, comm, deptno);

    COMMIT;

EXCEPTION
    WHEN error_emp_rep THEN
        RAISE_APPLICATION_ERROR(-20104, 'El número de empleado ya existe');

    WHEN OTHERS THEN
        ROLLBACK;
        RAISE_APPLICATION_ERROR(-20004, 'Error desconocido en la operación de inserción de empleado');
END;
/
