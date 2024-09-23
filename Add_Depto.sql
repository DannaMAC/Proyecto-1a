SET SERVEROUTPUT ON;

CREATE OR REPLACE PROCEDURE add_depto(
  no_dept NUMBER,
  name_dept VARCHAR,
  location_dept VARCHAR)
IS
  no_cont NUMBER;
  error_dept_10 EXCEPTION;
  error_dept_rep EXCEPTION;
BEGIN
  SELECT COUNT(*)
  INTO no_cont
  FROM dept
  WHERE deptno = no_dept;
  IF no_cont > 0 THEN
    RAISE error_dept_rep;
  END IF;
  INSERT INTO dept (deptno, dname, loc) VALUES (no_dept, name_dept,
  location_dept);
  IF MOD(no_dept,10) <> 0 THEN
    RAISE error_dept_10;
  END IF;
  COMMIT;
EXCEPTION
  WHEN error_dept_10 THEN
    RAISE_APPLICATION_ERROR(-20101, 'El departamento no es divisible entre 10');
  WHEN error_dept_rep THEN
    RAISE_APPLICATION_ERROR(-20102, 'El numero de departamento ya existe');
END;