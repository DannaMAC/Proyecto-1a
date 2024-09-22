import cx_Oracle

conn = cx_Oracle.connect('scott/scott@//localhost:1521/xepdb1')

cur = conn.cursor()

def add_depto():
    print("Ingresa el numero de departamento: ")
    deptno = int(input())
    print("Ingresa el nombre del departamento: ")
    dname = input()
    print("Ingresa el nombre de la localidad: ")
    loc = input()
    try:
        cur.callproc('add_depto',(deptno, dname, loc))
        print("Ejecutado con exito")
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        if error.code == 20100:
            print("Error: tal")
        else:
            print("Error: ", error.message)

def update_depto():
    print("en proceso...")

def delete_depto():
    print("en proceso...")

def add_emp():
    print("en proceso...")

def delete_emp():
    print("en proceso...")

def update_emp():
    print("en proceso...")

def noEmp_depto():
    print("en proceso...")

opcion = 0
while opcion != 8:
    print("Bienvenidos al Proyecto 1a de Python y SQL")
    print("1- Agregar departamento")
    print("2- Actualizar departamento")
    print("3- Eliminar departamento")
    print("4- Agregar empleado")
    print("5- Eliminar empleado")
    print("6- Actualizar empleado")
    print("7- Ver numero de empleados de un departamento")
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
            
