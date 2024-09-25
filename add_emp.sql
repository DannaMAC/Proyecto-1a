SET SERVEROUTPUT ON;

CREATE OR REPLACE PROCEDURE add_emp (
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
    error_emp_rep EXCEPTION;
BEGIN
    SELECT COUNT(*)
    INTO no_cont
    FROM EMP
    WHERE EMPNO = emp_no;

    IF no_cont > 0 THEN
        RAISE error_emp_rep;
    END IF;

    INSERT INTO EMP (EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO)
    VALUES (emp_no, e_name, e_job, e_mgr, e_hiredate, e_sal, e_comm, e_deptno);

    COMMIT;

EXCEPTION
    WHEN error_emp_rep THEN
        RAISE_APPLICATION_ERROR(-20104, 'El número de empleado ya existe');

    WHEN OTHERS THEN
        ROLLBACK;
        RAISE_APPLICATION_ERROR(-20004, 'Error desconocido en la operación de inserción de empleado');
END;
/
