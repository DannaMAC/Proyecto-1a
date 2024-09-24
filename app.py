import cx_Oracle

conn = cx_Oracle.connect('scott/scott@//localhost:1521/xepdb1')
cur = conn.cursor()

def add_depto():
    print("Ingresa el número de departamento: ")
    deptno = int(input())
    print("Ingresa el nombre del departamento: ")
    dname = input()
    print("Ingresa el nombre de la localidad: ")
    loc = input()
    try:
        cur.callproc('add_depto', (deptno, dname, loc))
        print("Departamento agregado con éxito")
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        print("Error: ", error.message)

def update_depto():
    print("Ingresa el número de departamento a actualizar: ")
    deptno = int(input())
    print("Ingresa el nuevo nombre del departamento: ")
    dname = input()
    print("Ingresa la nueva localidad: ")
    loc = input()
    try:
        cur.callproc('update_depto', (deptno, dname, loc))
        print("Departamento actualizado con éxito")
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        print("Error: ", error.message)

def delete_depto():
    print("Ingresa el número de departamento a eliminar: ")
    deptno = int(input())
    try:
        cur.callproc('delete_depto', [deptno])
        print("Departamento eliminado con éxito")
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        print("Error: ", error.message)

def add_emp():
    print("Ingresa el número de empleado: ")
    empno = int(input())
    print("Ingresa el nombre del empleado: ")
    ename = input()
    print("Ingresa el número de departamento: ")
    deptno = int(input())
    print("Ingresa el salario: ")
    sal = float(input())
    try:
        cur.callproc('add_emp', (empno, ename, deptno, sal))
        print("Empleado agregado con éxito")
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        print("Error: ", error.message)

def delete_emp():
    print("Ingresa el número de empleado a eliminar: ")
    empno = int(input())
    try:
        cur.callproc('delete_emp', [empno])
        print("Empleado eliminado con éxito")
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        print("Error: ", error.message)

def update_emp():
    print("Ingresa el número de empleado a actualizar: ")
    empno = int(input())
    print("Ingresa el nuevo nombre del empleado: ")
    ename = input()
    print("Ingresa el nuevo salario: ")
    sal = float(input())
    try:
        cur.callproc('update_emp', (empno, ename, sal))
        print("Empleado actualizado con éxito")
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        print("Error: ", error.message)

def noEmp_depto():
    print("Ingresa el número de departamento: ")
    deptno = int(input())
    try:
        cur.execute('SELECT COUNT(*) FROM empleados WHERE deptno = :deptno', deptno=deptno)
        count = cur.fetchone()[0]
        print(f"El número de empleados en el departamento {deptno} es {count}")
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        print("Error: ", error.message)

opcion = 0
while opcion != 8:
    print("\nBienvenidos al Proyecto 1a de Python y SQL")
    print("1- Agregar departamento")
    print("2- Actualizar departamento")
    print("3- Eliminar departamento")
    print("4- Agregar empleado")
    print("5- Eliminar empleado")
    print("6- Actualizar empleado")
    print("7- Ver número de empleados de un departamento")
    print("8- Salir")
    opcion = int(input())

    match opcion:
        case 1:
            add_depto()
        case 2:
            update_depto()
        case 3:
            delete_depto()
        case 4:
            add_emp()
        case 5:
            delete_emp()
        case 6:
            update_emp()
        case 7:
            noEmp_depto()
        case 8:
            print("Saliendo...")

cur.close()
conn.close()
