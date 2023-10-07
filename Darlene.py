from random import randint
# Lista para almacenar los errores
log_errores = []
# Función para registrar un error en el log
def registrar_error(tipo_error, funcion, descripcion):
    import datetime
    hora_error = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_errores.append((hora_error, tipo_error, funcion, descripcion))
# Se llena la matriz salas con elementos en el siguiente orden:
# Cantidad de filas, cantidad de columnas, nombre de la película, día de reproducción y hora de la misma
salas = [[3, 3, 'Venom', 4, 6],[4, 4, 'Cars', 5, 2],[5, 5, 'Avatar', 12, 7]]
def mostrar_salas():
    try:
        for i in range(len(salas)):
            if len(salas[i]) < 4:
                raise ValueError("La sala {} no tiene información completa.".format(i + 1))
            
            print("Sala", i + 1)
            print("Película  Día  Hora")
            for j in range(len(salas[i]) - 3, len(salas[i])):
                print(salas[i][j], end="      ")
            print()
            print()    
    except Exception as e:
        registrar_error("Error en mostrar_salas", "mostrar_salas", str(e))
# Se crea la función modificacion_sala para crear nuevos elementos y llenar una nueva lista que será añadida a la matriz.
def modificacion_sala(sala_nueva):
    try:
        tamaño_fila_sala = int(input("Ingrese el tamaño de filas de la sala: "))
        if tamaño_fila_sala <= 0:
            raise ValueError("El tamaño de filas debe ser mayor a cero.")
        sala_nueva.append(tamaño_fila_sala)
        
        tamaño_columna_sala = int(input("Ingrese el tamaño de columnas de la sala: "))
        if tamaño_columna_sala <= 0:
            raise ValueError("El tamaño de columnas debe ser mayor a cero.")
        sala_nueva.append(tamaño_columna_sala)
        
        pelicula = str(input("Ingrese la película a proyectar: "))
        if not pelicula:
            raise ValueError("El nombre de la película no puede estar vacío.")
        sala_nueva.append(pelicula)
        
        fecha = int(input("Ingrese la fecha en la que se va a reproducir la película: "))
        if fecha < 0 or fecha > 31:
            raise ValueError("La fecha ingresada no es válida.")
        sala_nueva.append(fecha)
        
        hora = int(input("Ingrese la hora en la que se va a reproducir la película: "))
        if hora < 0 or hora > 24:
            raise ValueError("La hora ingresada no es válida.")
        sala_nueva.append(hora)

        return sala_nueva
    
    except ValueError as ve:
        registrar_error("Error en modificacion_sala", "modificacion_sala", str(ve))
# Se crea la función configuracion_sala para modificar o crear una nueva sala, dependiendo de la opción que escoja el usuario.
def configuracion_sala():
    try:
        print("Configuración")
        print()
        print("1.- Definir nueva sala.")
        print("2.- Modificar sala existente.")
        print()
        opc = int(input("Ingrese la opción con la que desea trabajar: "))
        print()
        while opc != 1 and opc != 2:
            print()
            print("Error.")
            print("Opción inválida.")
            opc = int(input("Ingrese la opción con la que desea trabajar: "))
            print()
        if opc == 1:
            nueva_sala = []
            modificacion_sala(nueva_sala)
            salas.append(nueva_sala)
            print()
            print("La nueva sala se creó exitosamente.")
            print()
            mostrar_salas()      
        else:
            mostrar_salas()
            opc = int(input("Ingrese el número de la sala que desea modificar: "))
            print()
            for x in range(0, len(salas)):
                if opc - 1 == x:
                    salas.insert(x, modificacion_sala(salas[x]))
                    salas.remove(salas[x + 1])
            print()
            print("La sala", opc, "fue modificada correctamente.")
            print()
            mostrar_salas()

    except ValueError as ve:
        registrar_error("Error en configuracion_sala", "configuracion_sala", str(ve))

# Se crea la función mostrar_matriz para visualizar por pantalla la matriz de asientos disponibles y ocupados.
def mostrar_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()
# Se crea la función crear_matriz para crear una matriz basada en los datos de la lista de cada sala.
from random import randint
def crear_matriz(filas, columnas):
    try:
        matriz = []
        for x in range(filas):
            fila = []
            for y in range(columnas):
                a = int(input(f"Ingrese un número entero para la fila {x + 1}, columna {y + 1}: "))
                fila.append(a)                   
            matriz.append(fila)
        return matriz
    
    except ValueError:
        raise ValueError("Ingresaste una cadena de caracteres, ingresa un número entero.")

# Se crea la función reservacion_asientos para modificar el contenido de la matriz, logrando así completar
# la reservación de asiento del usuario.
def reservacion_asientos():
    try:
        mostrar_salas()
        opc = int(input("Ingrese el número de la sala a la que desea ir: "))
        print()
        for x in range(0, len(salas)):
            if opc - 1 == x:
                fila = salas[x][0]
                columna = salas[x][1]        
        matriz = crear_matriz(fila, columna)
        print("Se mostrarán los asientos ocupados con 1 (uno) y los disponibles con 0 (cero).")
        print()
        mostrar_matriz(matriz)
        print()
        fila_mod = int(input("Ingrese el número de fila del asiento que desea reservar: "))
        columna_mod = int(input("Ingrese el número de columna del asiento que desea reservar: "))     
        while (fila_mod < 0 or fila_mod >= fila or columna_mod < 0 or columna_mod >= columna):
            print()
            print("Valores fuera de rango.")
            print("Intente de nuevo.")
            fila_mod = int(input("Ingrese el número de fila del asiento que desea reservar: "))
            columna_mod = int(input("Ingrese el número de columna del asiento que desea reservar: "))       
        while (matriz[fila_mod][columna_mod] == 1):
            print()
            print("Asiento ocupado.")
            print("Intente de nuevo.")
            fila_mod = int(input("Ingrese el número de fila del asiento que desea reservar: "))
            columna_mod = int(input("Ingrese el número de columna del asiento que desea reservar: "))      
        print()
        matriz[fila_mod][columna_mod] = 1
        print("La distribución de asientos luego de su reserva:")
        print()
        mostrar_matriz(matriz)
        print()
        print("Gracias por su compra.")   
    except ValueError as ve:
        registrar_error("Error en reservacion_asientos", "reservacion_asientos", str(ve))
    # Clase Empleado para representar a cada empleado
class Empleado:
    def __init__(self, nombre, apellido, correo, cedula, direccion, fecha_contratacion, cargo, estatus):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.cedula = cedula
        self.direccion = direccion
        self.fecha_contratacion = fecha_contratacion
        self.cargo = cargo
        self.estatus = estatus
# Lista para almacenar a los empleados
empleados = []
# Función para crear un nuevo empleado
def crear_empleado():
    try:
        nombre = input("Ingrese el nombre del empleado: ")
        if not nombre:
            raise ValueError("El nombre del empleado no puede estar vacío.")   
        apellido = input("Ingrese el apellido del empleado: ")
        if not apellido:
            raise ValueError("El apellido del empleado no puede estar vacío.")      
        correo = input("Ingrese el correo electrónico del empleado: ")
        if not correo:
            raise ValueError("El correo electrónico del empleado no puede estar vacío.")       
        cedula = input("Ingrese la cédula del empleado: ")
        if not cedula:
            raise ValueError("La cédula del empleado no puede estar vacía.")      
        direccion = input("Ingrese la dirección del empleado: ")      
        fecha_contratacion = input("Ingrese la fecha de contratación del empleado (dd/mm/yyyy): ")       
        cargo = input("Ingrese el cargo del empleado: ")       
        estatus = input("Ingrese el estatus del empleado (activo/inactivo): ") 
        empleado = Empleado(nombre, apellido, correo, cedula, direccion, fecha_contratacion, cargo, estatus)
        empleados.append(empleado)
        print("El empleado se ha creado exitosamente.")  
    except ValueError as ve:
        registrar_error("Error en crear_empleado", "crear_empleado", str(ve))
# Función para buscar un empleado por su cédula
def buscar_empleado():
    cedula = input("Ingrese la cédula del empleado que desea buscar: ")

    for empleado in empleados:
        if empleado.cedula == cedula:
            print("Empleado encontrado:")
            print("Nombre:", empleado.nombre)
            print("Apellido:", empleado.apellido)
            print("Correo electrónico:", empleado.correo)
            print("Cédula:", empleado.cedula)
            print("Dirección:", empleado.direccion)
            print("Fecha de contratación:", empleado.fecha_contratacion)
            print("Cargo:", empleado.cargo)
            print("Estatus:", empleado.estatus)
            return

    print("No se encontró ningún empleado con la cédula ingresada.")

# Función para eliminar un empleado por su cédula
def eliminar_empleado():
    cedula = input("Ingrese la cédula del empleado que desea eliminar: ")

    empleado_encontrado = None

    for empleado in empleados:
        if empleado.cedula == cedula:
            empleado_encontrado = empleado
            break

    if empleado_encontrado is not None:
        empleados.remove(empleado_encontrado)
        print("El empleado se ha eliminado exitosamente.")
    else:
        print("No se encontró ningún empleado con la cédula ingresada.")


# Función para modificar los datos de un empleado por su cédula
def modificar_empleado():
    cedula = input("Ingrese la cédula del empleado que desea modificar: ")
    empleado_encontrado = None

    for empleado in empleados:
        if empleado.cedula == cedula:
            empleado_encontrado = empleado
            break

    if empleado_encontrado is not None:
        print("Empleado encontrado. Ingrese los nuevos datos:")
        empleado_encontrado.nombre = input("Ingrese el nuevo nombre del empleado: ")
        empleado_encontrado.apellido = input("Ingrese el nuevo apellido del empleado: ")
        empleado_encontrado.correo = input("Ingrese el nuevo correo electrónico del empleado: ")
        empleado_encontrado.direccion = input("Ingrese la nueva dirección del empleado: ")
        empleado_encontrado.fecha_contratacion = input("Ingrese la nueva fecha de contratación del empleado (dd/mm/yyyy): ")
        empleado_encontrado.cargo = input("Ingrese el nuevo cargo del empleado: ")
        empleado_encontrado.estatus = input("Ingrese el nuevo estatus del empleado (activo/inactivo): ")
        print("Los datos del empleado se han modificado exitosamente.")
    else:
        print("No se encontró ningún empleado con la cédula ingresada.")

# Función para consultar todos los empleados
def consultar_empleados():
    if len(empleados) == 0:
        print("No hay empleados registrados.")
        return

    print("Lista de empleados:")
    for empleado in empleados:
        print("Nombre:", empleado.nombre)
        print("Apellido:", empleado.apellido)
        print("Correo electrónico:", empleado.correo)
        print("Cédula:", empleado.cedula)
        print("Dirección:", empleado.direccion)
        print("Fecha de contratación:", empleado.fecha_contratacion)
        print("Cargo:", empleado.cargo)
        print("Estatus:", empleado.estatus)
        print()

# Función para mostrar el menú de opciones
def submenu():
    while True:
        try:
            print("\n--- Gestión de Empleados ---")
            print("1. Crear empleado")
            print("2. Buscar empleado")
            print("3. Eliminar empleado")
            print("4. Modificar empleado")
            print("5. Consultar empleados")
            print("6. Salir")

            opcion = input("Ingrese el número de la opción que desea ejecutar: ")

            if opcion == "1":
                crear_empleado()
            elif opcion == "2":
                buscar_empleado()
            elif opcion == "3":
                eliminar_empleado()
            elif opcion == "4":
                modificar_empleado()
            elif opcion == "5":
                consultar_empleados()
            elif opcion == "6":
                print("Gracias por utilizar el sistema de gestión de empleados.")
                break
            else:
                print("Opción inválida. Por favor, ingrese un número válido.")
        
        except ValueError:
            print("Error: No ingresaste un número, eso es un carácter.")
        except Exception as e:
            registrar_error("Error en submenu", "submenu", str(e))

# Clase Pago para representar cada pago
class Pago:
    def __init__(self, nombre_cliente, apellido_cliente, cedula_cliente, correo_cliente, pelicula, sala, cantidad_asientos, ubicacion_asientos, fecha_pago, forma_pago):
        self.nombre_cliente = nombre_cliente
        self.apellido_cliente = apellido_cliente
        self.cedula_cliente = cedula_cliente
        self.correo_cliente = correo_cliente
        self.pelicula = pelicula
        self.sala = sala
        self.cantidad_asientos = cantidad_asientos
        self.ubicacion_asientos = ubicacion_asientos
        self.fecha_pago = fecha_pago
        self.forma_pago = forma_pago

# Lista para almacenar los pagos
pagos = []

# Función para crear un nuevo pago
def crear_pago():
    try:
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        if not nombre_cliente:
            raise ValueError("Error: Debes ingresar el nombre del cliente.")
        
        apellido_cliente = input("Ingrese el apellido del cliente: ")
        if not apellido_cliente:
            raise ValueError("Error: Debes ingresar el apellido del cliente.")
        
        cedula_cliente = input("Ingrese la cédula del cliente: ")
        if not cedula_cliente:
            raise ValueError("Error: Debes ingresar la cédula del cliente.")
        
        correo_cliente = input("Ingrese el correo electrónico del cliente: ")
        if not correo_cliente:
            raise ValueError("Error: Debes ingresar el correo electrónico del cliente.")
        
        pelicula = input("Ingrese el nombre de la película: ")
        sala = input("Ingrese el número de sala: ")
        
        cantidad_asientos = int(input("Ingrese la cantidad de asientos: "))
        if cantidad_asientos <= 0:
            raise ValueError("Error: La cantidad de asientos debe ser mayor a cero.")
        
        ubicacion_asientos = []
        for i in range(cantidad_asientos):
            ubicacion = input(f"Ingrese la ubicación del asiento {i + 1}: ")
            ubicacion_asientos.append(ubicacion)
        
        fecha_pago = input("Ingrese la fecha de pago (dd/mm/yyyy): ")
        forma_pago = input("Ingrese la forma de pago: ")
        
        pago = Pago(nombre_cliente, apellido_cliente, cedula_cliente, correo_cliente, pelicula, sala, cantidad_asientos, ubicacion_asientos, fecha_pago, forma_pago)
        pagos.append(pago)
        
        print("El pago se ha registrado exitosamente.")
    
    except ValueError as ve:
        print(ve)
        registrar_error("Error en crear_pago", "crear_pago", str(ve))
    except Exception as e:
        registrar_error("Error en crear_pago", "crear_pago", str(e))


# Función para validar que los asientos estén marcados previamente
def validar_asientos():
    try:
        sala = input("Ingrese el número de sala: ")
        asientos_marcados = set()

        for pago in pagos:
            if pago.sala == sala:
                for ubicacion in pago.ubicacion_asientos:
                    asientos_marcados.add(ubicacion)

        cantidad_asientos = int(input("Ingrese la cantidad de asientos a validar: "))
        asientos_validos = []

        for i in range(cantidad_asientos):
            ubicacion = input(f"Ingrese la ubicación del asiento {i+1}: ")
            if ubicacion in asientos_marcados:
                asientos_validos.append(ubicacion)

        if not asientos_validos:
            print("Ninguno de los asientos ingresados es válido.")
        else:
            print("Asientos válidos:")
            for ubicacion in asientos_validos:
                print(ubicacion)
    
    except ValueError as ve:
        print(f"Error: {ve}")
        registrar_error("Error en validar_asientos", "validar_asientos", str(ve))
    except Exception as e:
        registrar_error("Error en validar_asientos", "validar_asientos", str(e))


# Función para generar una factura por cada reservación
def generar_facturas():
    for pago in pagos:
        print("Factura:")
        print("Nombre:", pago.nombre_cliente)
        print("Apellido:", pago.apellido_cliente)
        print("Cédula:", pago.cedula_cliente)
        print("Correo electrónico:", pago.correo_cliente)
        print("Película:", pago.pelicula)
        print("Sala:", pago.sala)
        print("Cantidad de asientos:", pago.cantidad_asientos)
        print("Ubicación de asientos:", pago.ubicacion_asientos)
        print("Fecha de pago:", pago.fecha_pago)
        print("Forma de pago:", pago.forma_pago)
        print()

# Función para listar todos los pagos realizados
def listar_pagos():
    if len(pagos) == 0:
        print("No hay pagos registrados.")
        return

    print("Lista de pagos:")
    for pago in pagos:
        print("Nombre:", pago.nombre_cliente)
        print("Apellido:", pago.apellido_cliente)
        print("Cédula:", pago.cedula_cliente)
        print("Correo electrónico:", pago.correo_cliente)
        print("Película:", pago.pelicula)
        print("Sala:", pago.sala)
        print("Cantidad de asientos:", pago.cantidad_asientos)
        print("Ubicación de asientos:", pago.ubicacion_asientos)
        print("Fecha de pago:", pago.fecha_pago)
        print("Forma de pago:", pago.forma_pago)
        print()

# Función para mostrar el menú de opciones
def submenu2():
    while True:
        print("\n--- Gestión de Pagos y Facturas ---")
        print("1. Crear pago")
        print("2. Validar asientos")
        print("3. Generar facturas")
        print("4. Listar pagos")
        print("5. Salir")

        opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == "1":
            crear_pago()
        elif opcion == "2":
            validar_asientos()
        elif opcion == "3":
            generar_facturas()
        elif opcion == "4":
            listar_pagos()
        elif opcion == "5":
            print("Gracias por utilizar el sistema de gestión de pagos y facturas.")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")
          
# Se crea la función menu para controlar la interfaz de usuario, repitiéndose siempre hasta que se cierre sesión.
def menu():
    while(True):
        print()
        print("\tBienvenido al cine.")
        print()
        print("Menú Principal:")
        print()
        print("1.- Administrador.")
        print("2.- Cliente.")
        print()
        opc = int(input("Ingrese el número correspondiente al tipo de usuario: "))
        print()

        if (opc == 1):
            print("1.- Configuración de Salas.")
            print("2.- Salas existentes.")
            print("3.- Reservación de asientos.")
            print("4.- Gestion de empleados.")
            print("5.- Gestion de pagos y facturas.")
            print("6.- Cerrar sesión.")
            
            print()
            opc_adm = int(input("Ingrese la opción con la que desea trabajar: "))
            print()
            while (opc_adm < 1 and opc_adm > 6):
                print("Error.")
                print("Opción inválida.")
                opc_adm = int(input("Ingrese la opción con la que desea trabajar: "))

            if (opc_adm == 1):
                configuracion_sala()
            if (opc_adm == 2):
                mostrar_salas()
            if (opc_adm == 3):
                reservacion_asientos()
            if (opc_adm == 4):
                submenu()    
            if (opc_adm == 5):
                submenu2()  
            if (opc_adm == 6):
                print("Gracias por su visita.")
                break
        
        if (opc == 2):
            print("1.- Salas existentes.")
            print("2.- Reservación de asientos.")
            print("3.- Cerrar sesión.")
            print()
            opc_clt = int(input("Ingrese la opción con la que desea trabajar: "))
            print()
            while (opc_clt < 1 and opc_clt > 3):
                print("Error.")
                print("Opción inválida.")
                opc_clt = int(input("Ingrese la opción con la que desea trabajar: "))

            if (opc_clt == 1):
                mostrar_salas()

            if (opc_clt == 2):
                reservacion_asientos()
                
            if (opc_clt == 3):
                print("Gracias por su visita.")
                break

# Se llama a la función para que se ejecute el programa.
menu()