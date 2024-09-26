import cx_Oracle

conn = cx_Oracle.connect('scott/scott@//localhost:1521/xepdb1')
cur = conn.cursor()


#region CRUD
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
        error_message = error.message.split('\n')[0]
        if error.code == 20101:
            print("Error: El departamento no es divisible entre 10")
        elif error.code == 20102:
            print("Error: El numero de departamento ya existe")
        else:
            print("Error: ", error_message)

def update_depto():
    print("Ingresa el número de departamento a actualizar: ")
    deptno = int(input())
    print("1- Nombre del departamento")
    print("2- Localidad")
    print("3- Salir")
    opcion = int(input())
    field = ""
    new = 0
    match opcion:
        case 1:
            print("Ingresa el nuevo nombre del departamento: ")
            new = input()
            field = "DNAME"
        case 2:
            print("Ingresa la nueva localidad: ")
            new = input()
            field = "LOC"
        case 3:
            print("Saliendo...")
    try:
        cur.callproc('update_depto', (deptno, field, new))
        print("Departamento actualizado con éxito")
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        error_message = error.message.split('\n')[0]
        if error.code == 20103:
            print("Error: El departamento no existe")
        else:
            print("Error: ", error_message)

def delete_depto():
    print("Ingresa el número de departamento a eliminar: ")
    deptno = int(input())
    try:
        cur.callproc('delete_depto', [deptno])
        print("Departamento eliminado con éxito")
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        error_message = error.message.split('\n')[0]
        if error.code == 20106:
            print("Error: El empleado no existe")
        else: 
            print("Error: ", error)

def add_emp():
    print("Ingresa el número de empleado: ")
    empno = int(input())
    print("Ingresa el nombre del empleado: ")
    ename = input()
    print("Escribe el trabajo del empleado: ")
    job = input()
    print("Escribe el id del manager del empleado: ")
    mgr = validate_null_input(input())
    print("Escribe el dia de contratacion: ")
    day = int(input())
    print("Escribe el mes de contratacion: ")
    month = validate_month(input())
    print("Escribe el año de contratacion: ")
    year = validate_year(input())
    print("Ingresa el salario: ")
    sal = int(input())
    print("Escribe la comision del empleado: ")
    comm = validate_null_input(input())
    print("Ingresa el número de departamento: ")
    deptno = int(input())
    
    date = (f"{day}-{month}-{year}")
    try:
        cur.callproc('add_emp', (empno, ename, job, mgr, date, sal, comm, deptno))
        print("Empleado agregado con éxito")
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        error_message = error.message.split('\n')[0]
        if error.code == 20104:
            print("Error: El número de empleado ya existe")
        else:
            print("Error: ", error_message)

def delete_emp():
    print("Ingresa el número de empleado a eliminar: ")
    empno = int(input())
    try:
        cur.callproc('delete_emp', [empno])
        print("Empleado eliminado con éxito")
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        error_message = error.message.split('\n')
        if error.code == 20106:
            print("El empleado no existe")
        else:
            print("Error: ", error_message)

# TODO: VERIFICAR QUE EL MANAGER EXISTA
# TODO: VERIFICAR QUE EL SALARIO SEA MAYOR A 0
# TODO: VERIFICAR QUE LA FK (NUMERO DE DEPARTAMENTO, NADA MÁS VERIFICAR QUE EXISTA)
def update_emp():
    print("Ingresa el número de empleado a actualizar: ")
    empno = int(input())

    if (validate_employee_existance(empno) == 1):
        print("1- Nombre")
        print("2- Trabajo")
        print("3- Manager")
        print("4- Fecha de Contratacion")
        print("5- Salario")
        print("6- Comision")
        print("7- Numero de departamento")
        print("8- Salir")
        opcion = int(input())
        field = ""
        new = 0
        match opcion:
            case 1:
                print("Ingresa el nuevo nombre del empleado: ")
                new = input()
                field = "ENAME"
            case 2:
                print("Escribe el nuevo trabajo del empleado: ")
                new = input()
                field = "JOB"
            case 3:
                print("Escribe el nuevo id del manager del empleado: ")
                inp = validate_null_input(input())

                if (inp != None or validate_employee_existance(inp) != 1):
                    print("El empleado especificado no existe")
                else:
                    new = inp
                    field = "MGR"
            case 4:
                print("Escribe el nuevo dia de contratacion: ")
                day = int(input())
                print("Escribe el nuevo mes de contratacion: ")
                month = validate_month(input())
                print("Escribe el nuevo año de contratacion: ")
                year = validate_year(input())
                new = (f"{day}-{month}-{year}")
                field = "HIREDATE"
            case 5:
                print("Ingresa el nuevo salario: ")
                new = int(input())
                field = "SAL"
            case 6:
                print("Escribe la nueva comision del empleado: ")
                new = validate_null_input(input())
                field = "COMM"
            case 7:
                print("Ingresa el nuevo número de departamento: ")
                new = int(input())
                field = "DEPTNO"
            case 8:
                print("Saliendo...")
    else:
        print("El empleado no existe")

def noEmp_depto():
    print("Ingresa el número de departamento: ")
    deptno = int(input())
    try:
        count = cur.callfunc('noemp_depto',cx_Oracle.NUMBER, [deptno])
        print(f"El número de empleados en el departamento {deptno} es {int(count)}")
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        error_message = error.message.split('\n')
        if error.code == 20107:
            print("Error: El departamento no tiene empleados asociados")
        else: 
            print("Error: ", error_message)
#endregion


#region Verification Methods
def validate_null_input(user_input):
    if (user_input == ''):
        user_input = None
    else:
        user_input = int(user_input)
    return user_input

def validate_month(user_input):
    month_map = {
        '1': 'JAN',
        '2': 'FEB',
        '3': 'MAR',
        '4': 'APR',
        '5': 'MAY',
        '6': 'JUN',
        '7': 'JUL',
        '8': 'AUG',
        '9': 'SEP',
        '10': 'OCT',
        '11': 'NOV',
        '12': 'DEC'
    }

    if user_input.isdigit() and str(int(user_input)) in month_map:
        return month_map[str(int(user_input))]
    else:
        if len(user_input) >= 3:
            return user_input[:3].upper()
        else:
            return user_input

def validate_year(user_input):
    if (len(user_input) >= 2):
        return user_input[-2:]
    return int(user_input)

def validate_employee_existance(user_input):
    empno = int(user_input)
    try:
        ex = cur.callfunc('check_employee_exists',cx_Oracle.NUMBER, [empno])
        return 1
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        error_message = error.message.split('\n')
        if error.code == -20106:
            print("Error: El empleado no existe")
        else:
            print("Error: ", error_message)
        return 0

def validate_department_existance(user_input):
    deptno = int(user_input)
    try:
        ex = cur.callfunc('check_department_exists',cx_Oracle.NUMBER, [deptno])
        return 1
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        error_message = error.message.split('\n')
        if error.code == -20106:
            print("Error: El departamento no existe")
        else:
            print("Error: ", error_message)
        return 0
#endregion


# region Main
opcion = 0
while opcion != 8:
    print("\nBienvenido al Proyecto 1a de Python y SQL")
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
        case 9:
            while(1):
                empno = int(input())
                if (validate_department_existance(empno) == 1):
                    print("hola")
                else:
                    print("no")

cur.close()
conn.close()
#endregion
