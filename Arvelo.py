# MOdulo de Menú de opciones
def mostrar_menu():
        print("Menú de Opciones")
        print("----------------")
        print("1. Configuración de Salas")
        print("2. Reservación de Asientos")
        print("3. Reportes")
        print("4. Modificar sala")
        print("5. Gestión de Empleados")
        print("6. Gestionar Pagos")
        print("7. Salir")

def ejecutar_opcion(opcion, salas):
        if opcion == 1:
            configurar_salas(salas)
        elif opcion == 2:
            reservar_asiento(salas)
        elif opcion == 3:
            mostrar_reportes(salas)
        elif opcion == 4:
            modificar_sala(salas)
        elif opcion == 5:
            gestionar_empleados(empleados)
        elif opcion == 6:
            gestionar_pagos(pagos, salas)
        elif opcion == 7:
            print("¡Hasta luego!")
            return False
        else:
            print("Opción inválida.")
        return True

# Modulo modificar_sala
def modificar_sala(salas):
        print("Modificar Sala")
        print("--------------")
        sala_id = int(input("Ingrese el numero de sala que desea modificar: "))
    
        if sala_id >= 1 and sala_id <= len(salas):
            sala = salas[sala_id - 1]
            print(f"Sala {sala_id}:")
            print(f"Pelicula: {sala['pelicula']}")
            print(f"Fecha: {sala['fecha']}")
            print(f"Hora: {sala['hora']}")
            print(f"Descripción: {sala['descripcion']}")
            print(f"Cantidad de Asientos Vacíos: {sala['cantidad_vacios']}")
        
            opcion = input("¿Desea modificar la sala? (s/n): ")
        
            if opcion.lower() == "s":
                pelicula = input("Ingrese el nuevo nombre de la película: ")
                fecha = input("Ingrese la nueva fecha de la funcion: ")
                hora = input("Ingrese la nueva hora de la funcion: ")
                descripcion = input("Ingrese una nueva descripción de la sala: ")
            
                sala["pelicula"] = pelicula
                sala["fecha"] = fecha
                sala["hora"] = hora
                sala["descripcion"] = descripcion
            
                print("Sala modificada exitosamente!")
            else:
                print("No se realizaron modificaciones.")
        else:
            print("Número de sala inválido.")

# Módulo de reportes
def mostrar_reportes(salas):
        print("Salas existentes:")
        for sala in salas:
            print(f"   Película: {sala['pelicula']}, Fecha: {sala['fecha']}, Hora: {sala['hora']}, Descripción: {sala['descripcion']}")
            print(f"   Cantidad de asientos vacíos: {sala['cantidad_vacios']}")

        peliculas = set([sala["pelicula"] for sala in salas])
        print("Películas existentes:")
        for pelicula in peliculas:
            print(f"   {pelicula}")

# Módulo de Configuración de Salas
def configurar_salas(salas):
        print("Configuración de Salas")
        print("----------------------")
        pelicula = input("Ingrese el nombre de la película: ")
        fecha = input("Ingrese la fecha de proyección: ")
        hora = input("Ingrese la hora de proyección: ")
        descripcion = input("Ingrese una descripción de la sala: ")
        n = int(input("Ingrese el tamaño de la sala (n x n): "))
        matriz_asientos = [[0] * n for _ in range(n)]
        sala = {
            "pelicula": pelicula,
            "fecha": fecha,
            "hora": hora,
            "descripcion": descripcion,
            "matriz_asientos": matriz_asientos,
            "cantidad_vacios": n * n
        }
        salas.append(sala)
        print("Sala configurada exitosamente!")

# Módulo de Reservación de asientos
def reservar_asiento(salas):
        print("Reservación de Asientos")
        print("-----------------------")
        print("Salas existentes:")
        for i, sala in enumerate(salas):
            print(f"{i+1}. Película: {sala['pelicula']}, Fecha: {sala['fecha']}, Hora: {sala['hora']}")
        sala_index = int(input("Seleccione una sala: ")) - 1
        if sala_index < 0 or sala_index >= len(salas):
            print("Selección de sala inválida.")
            return
        sala = salas[sala_index]
        matriz_asientos = sala["matriz_asientos"]
        print("Matriz de Asientos:")
        for fila in matriz_asientos:
            fila_str = " ".join(map(str, fila))
            fila_str = fila_str.replace("[", "").replace("]", "")
            print(fila_str)
        fila = int(input("Ingrese la posición de la fila del asiento a reservar: ")) - 1
        columna = int(input("Ingrese la posición de la columna del asiento a reservar: ")) - 1
        if fila < 0 or fila >= len(matriz_asientos) or columna < 0 or columna >= len(matriz_asientos[0]):
            print("Posición de asiento inválida.")
            return
        if matriz_asientos[fila][columna] == 1:
            print("El asiento seleccionado ya está ocupado.")
            return
        matriz_asientos[fila][columna] = 1
        sala["cantidad_vacios"] -= 1
        print("Asiento reservado exitosamente!")

# Módulo de Gestión de Empleados
def gestionar_empleados(empleados):
        print("Gestión de Empleados")
        print("--------------------")
        print("1. Crear Empleado")
        print("2. Buscar Empleado")
        print("3. Eliminar Empleado")
        print("4. Modificar Empleado")
        print("5. Consultar Empleado")
        print("6. Regresar al Menu Anterior")

        opcion = int(input("Seleccione una opción: "))
   
        if opcion == 1:
            crear_empleado(empleados)
        elif opcion == 2:
            buscar_empleado(empleados)
        elif opcion == 3:
            eliminar_empleado(empleados)
        elif opcion == 4:
            modificar_empleado(empleados)
        elif opcion == 5:
            consultar_empleado(empleados)
        elif opcion == 6:
            mostrar_menu()
        else:
            print("Opción inválida")

def validar_estatus(estatus):
    return estatus.lower() == "activo" or estatus.lower() == "inactivo"

def validar_cargo(cargo):
    cargos_validos = ["empleado general", "ayudante general de mantenimiento", "cajero", "gerente", "taquillero"]
    return cargo.lower() in cargos_validos

def crear_empleado(empleados):
    
        print("Crear Empleado")
        print("--------------")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        correo = input("Correo Electrónico: ")
        cedula = input("Cédula: ")
        direccion = input("Dirección: ")
        fecha_contratacion = input("Fecha de Contratación (dd/mm/yyyy): ")
        cargo = input("Cargo: ")
        while not validar_cargo(cargo):
            print("Cargo inválido. Intente nuevamente.")
            cargo = input("Cargo: ")
        estatus = input("Estatus (activo/inactivo): ")
        while not validar_estatus(estatus):
            print("Estatus inválido. Intente nuevamente.")
            estatus = input("Estatus (activo/inactivo): ")
        
        empleado = {
            "nombre": nombre,
            "apellido": apellido,
            "correo": correo,
            "cedula": cedula,
            "direccion": direccion,
            "fecha_contratacion": fecha_contratacion,
            "cargo": cargo,
            "estatus": estatus
        }
        
        empleados.append(empleado)
        
        print("Empleado creado exitosamente!")
        
def buscar_empleado(empleados):
            print("Buscar Empleado")
            print("---------------")
            cedula = input("Ingrese la cédula del empleado que desea buscar: ")
        
            for empleado in empleados:
                if empleado["cedula"] == cedula:
                    print("Empleado encontrado:")
                    print("Nombre:", empleado["nombre"])
                    print("Apellido:", empleado["apellido"])
                    print("Correo Electrónico:", empleado["correo"])
                    print("Cédula:", empleado["cedula"])
                    print("Dirección:", empleado["direccion"])
                    print("Fecha de Contratación:", empleado["fecha_contratacion"])
                    print("Cargo:", empleado["cargo"])
                    print("Estatus:", empleado["estatus"])
                    break
            else:
                print("Empleado no encontrado.")

def eliminar_empleado(empleados):
            print("Eliminar Empleado")
            print("-----------------")
            cedula = input("Ingrese la cédula del empleado que desea eliminar: ")
        
            for empleado in empleados:
                if empleado["cedula"] == cedula:
                    empleados.remove(empleado)
                    print("Empleado eliminado exitosamente!")
                    break
            else:
                print("Empleado no encontrado.")

def modificar_empleado(empleados):
            print("Modificar Empleado")
            print("------------------")
            cedula = input("Ingrese la cédula del empleado que desea modificar: ")
        
            for empleado in empleados:
                if empleado["cedula"] == cedula:
                    print("Empleado encontrado:")
                    print("Nombre:", empleado["nombre"])
                    print("Apellido:", empleado["apellido"])
                    print("Correo Electrónico:", empleado["correo"])
                    print("Cédula:", empleado["cedula"])
                    print("Dirección:", empleado["direccion"])
                    print("Fecha de Contratación:", empleado["fecha_contratacion"])
                    print("Cargo:", empleado["cargo"])
                    print("Estatus:", empleado["estatus"])
                
                    opcion = input("¿Desea modificar este empleado? (s/n): ")
                
                    if opcion.lower() == "s":
                        empleado["nombre"] = input("Nuevo Nombre: ")
                        empleado["apellido"] = input("Nuevo Apellido: ")
                        empleado["correo"] = input("Nuevo Correo Electrónico: ")
                        empleado["direccion"] = input("Nueva Dirección: ")
                        empleado["fecha_contratacion"] = input("Nueva Fecha de Contratación (dd/mm/yyyy): ")
                        empleado["cargo"] = input("Nuevo Cargo: ")
                        empleado["estatus"] = input("Nuevo Estatus (activo/inactivo): ")
                        print("Empleado modificado exitosamente!")
                    else:
                        print("No se realizaron modificaciones.")
                    break
            else:
                print("Empleado no encontrado.")

def consultar_empleado(empleados):
            print("Consultar Empleado")
            print("------------------")
            cedula = input("Ingrese la cédula del empleado que desea consultar: ")
        
            for empleado in empleados:
                if empleado["cedula"] == cedula:
                    print("Empleado encontrado:")
                    print("Nombre:", empleado["nombre"])
                    print("Apellido:", empleado["apellido"])
                    print("Correo Electrónico:", empleado["correo"])
                    print("Cédula:", empleado["cedula"])
                    print("Dirección:", empleado["direccion"])
                    print("Fecha de Contratación:", empleado["fecha_contratacion"])
                    print("Cargo:", empleado["cargo"])
                    print("Estatus:", empleado["estatus"])
                    break
            else:
                print("Empleado no encontrado.")

    
# Módulo de Gestión de Pagos y Facturas

def gestionar_pagos(pagos, salas):
            print("Gestión de Pagos y Facturas")
            print("--------------------------")
            print("1. Crear Pago")
            print("2. Modificar Pago")
            print("3. Eliminar Pago")
            print("4. Consultar Pago")
            print("5. Listar Pagos")
            print("6. Regresar al menu anterior")

            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                crear_pago(pagos, salas)
            elif opcion == 2:
                modificar_pago(pagos, salas)
            elif opcion == 3:
                eliminar_pago(pagos)
            elif opcion == 4:
                consultar_pago(pagos)
            elif opcion == 5:
                listar_pagos(pagos)
            elif opcion == 6:
                mostrar_menu()
            else:
                print("Opción inválida")

def crear_pago(pagos, salas):
            print("Crear Pago")
            print("----------")

            # Obtener información del pago
            nombre = input("Nombre del Cliente: ")
            apellido = input("Apellido del Cliente: ")
            cedula = input("Cédula del Cliente: ")
            correo = input("Correo del Cliente: ")
            pelicula = input("Película: ")
            sala = input("Sala: ")
            cantidad_asientos = int(input("Cantidad de Asientos: "))
            
            ubicacion_asientos = []
            
            for i in range(cantidad_asientos):
                fila = int(input(f"Ubicación de la fila del asiento {i+1}: "))
                columna = int(input(f"Ubicación de la columna del asiento {i+1}: "))
                ubicacion_asientos.append((fila, columna))
                fecha_pago_valida = False
                fecha_pago = input("Ingrese la fecha de pago (dd/mm/yyyy): ")
            forma_pago = input("Forma de Pago: ")
            if forma_pago.lower() not in ["efectivo", "punto de venta"]:
                print("La forma de pago ingresada no es válida.")
                return
            
            # Verificar si la sala existe
            sala_existente = False
            for sala in salas:
                if sala["descripcion"] == sala:
                    sala_existente = True
                    break

            if not sala_existente:
                print("La sala ingresada no existe.")
                return
            
            # Verificar si los asientos están marcados
            sala_asientos = sala["matriz_asientos"]
            for ubicacion in ubicacion_asientos.split(", "):
                fila, columna = ubicacion.split("-")
                fila = int(fila) - 1
                columna = int(columna) - 1
                if fila < 0 or fila >= len(sala_asientos) or columna < 0 or columna >= len(sala_asientos[0]) or sala_asientos[fila][columna] != 1:
                    print("Al menos uno de los asientos seleccionados no está disponible.")
                    return

            # Crear un nuevo pago
            pago = {
                "nombre": nombre,
                "apellido": apellido,
                "cedula": cedula,
                "correo": correo,
                "pelicula": pelicula,
                "sala": sala,
                "cantidad_asientos": cantidad_asientos,
                "ubicacion_asientos": ubicacion_asientos,
                "fecha_pago": fecha_pago,
                "forma_pago": forma_pago,
            }

            pagos.append(pago)
            print("Pago creado exitosamente!")
def modificar_pago(pagos, salas):
            print("Modificar Pago")
            print("--------------")
            cedula = input("Ingrese la cédula del cliente del pago que desea modificar: ")

            for pago in pagos:
                if pago["cedula"] == cedula:
                    print("Pago encontrado:")
                    print("Nombre:", pago["nombre"])
                    print("Apellido:", pago["apellido"])
                    print("Cédula:", pago["cedula"])
                    print("Película:", pago["pelicula"])
                    print("Sala:", pago["sala"])
                    print("Cantidad de Asientos:", pago["cantidad_asientos"])
                    print("Ubicación de los Asientos:", pago["ubicacion_asientos"])
                    print("Fecha de Pago:", pago["fecha_pago"])
                    print("Forma de Pago:", pago["forma_pago"])

                    opcion = input("¿Desea modificar este pago? (s/n): ")

                    if opcion.lower() == "s":
                        sala = input("Ingrese la nueva sala: ")
                        sala_existente = False
                        for sala in salas:
                            if sala["descripcion"] == sala:
                                sala_existente = True
                                break

                        if not sala_existente:
                            print("La sala ingresada no existe.")
                            return

                        # Verificar si los nuevos asientos están marcados
                        sala_asientos = sala["matriz_asientos"]
                        ubicacion_asientos = input("Ingrese la nueva ubicación de los asientos: ")
                        for ubicacion in ubicacion_asientos.split(", "):
                            fila, columna = ubicacion.split("-")
                            fila = int(fila) - 1
                            columna = int(columna) - 1
                            if fila < 0 or fila >= len(sala_asientos) or columna < 0 or columna >= len(sala_asientos[0]) or sala_asientos[fila][columna] != 1:
                                print("Al menos uno de los nuevos asientos seleccionados no está disponible.")
                                return

                        # Actualizar el pago con la nueva información
                        pago["sala"] = sala
                        pago["ubicacion_asientos"] = ubicacion_asientos

                        print("Pago modificado exitosamente!")
                    else:
                        print("No se realizaron modificaciones.")
                    break
            else:
                print("Pago no encontrado.")
def eliminar_pago(pagos):
            print("Eliminar Pago")
            print("-------------")
            cedula = input("Ingrese la cédula del cliente del pago que desea eliminar: ")

            for pago in pagos:
                if pago["cedula"] == cedula:
                    pagos.remove(pago)
                    print("Pago eliminado exitosamente!")
                    break
            else:
                print("Pago no encontrado.")
def consultar_pago(pagos):
            print("Consultar Pago")
            print("--------------")
            cedula = input("Ingrese la cédula del cliente del pago que desea consultar: ")

            for pago in pagos:
                if pago["cedula"] == cedula:
                    print("Pago encontrado:")
                    print("Nombre:", pago["nombre"])
                    print("Apellido:", pago["apellido"])
                    print("Cédula:", pago["cedula"])
                    print("Película:", pago["pelicula"])
                    print("Sala:", pago["sala"])
                    print("Cantidad de Asientos:", pago["cantidad_asientos"])
                    print("Ubicación de los Asientos:", pago["ubicacion_asientos"])
                    print("Fecha de Pago:", pago["fecha_pago"])
                    print("Forma de Pago:", pago["forma_pago"])
                    break
            else:
                print("Pago no encontrado.")
def listar_pagos(pagos):
            print("Listar Pagos")
            print("------------")
            for i, pago in enumerate(pagos):
                print(f"Pago {i+1}:")
                print("Nombre:", pago["nombre"])
                print("Apellido:", pago["apellido"])
                print("Cédula:", pago["cedula"])
                print("Película:", pago["pelicula"])
                print("Sala:", pago["sala"])
                print("Cantidad de Asientos:", pago["cantidad_asientos"])
                print("Ubicación de los Asientos:", pago["ubicacion_asientos"])
                print("Fecha de Pago:", pago["fecha_pago"])
                print("Forma de Pago:", pago["forma_pago"])
                print("---------------------------")
            print()

# Programa principal
salas = []
empleados = []
pagos = []
continuar = True
while continuar:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))
    continuar = ejecutar_opcion(opcion, salas)