empleados = []
import datetime
ahora = datetime.datetime.now()
logerror = []
csv = []
def configurar_salas():
    salas = []
    try:
        while True:
            nombreSala = input("Nombre de la sala (o * para salir): ")
            if nombreSala.lower() == "*":
                break  
            tamanoSala = int(input("Tamaño de la sala (nxn): "))
            pelicula = input("Película a proyectar: ")
            fechaHora = input("Fecha y hora de proyección: ")
            descripcion = input("Descripción de la sala: ")
            sala = {  
                "nombre": nombreSala,
                "tamano": tamanoSala,
                "pelicula": pelicula,
                "fechaHora": fechaHora,
                "descripcion": descripcion,
                "asientosDisponibles": [["O" for _ in range(tamanoSala)] for _ in range(tamanoSala)]
            }
            salas.append(sala)
        return salas
    except Exception as e:
        print("Porfavor ingrese un valor valido, reiniciando programa...")
        print("El error es:", e)
        error(e)
        logerror.append(error(e))

def reservar_asientos(salas):
    try:
        print("Salas disponibles:")
        for i, sala in enumerate(salas):
            print(str(i + 1) + ". " + sala["nombre"] + " - " + sala["pelicula"] + " - " + sala["fechaHora"])
            
        seleccion = int(input("Seleccione una sala: ")) - 1
        if seleccion < 0 or seleccion >= len(salas):
            print("Selección no válida.")
            return
        
        salaSeleccionada = salas[seleccion]
        tamanoSala = salaSeleccionada["tamano"]
        asientosDisponibles = salaSeleccionada["asientosDisponibles"]

        print("Asientos disponibles (O = Disponible, X = Ocupado):")
        try:
            for fila in asientosDisponibles:
                print(" ".join(fila))

            fila = int(input("Ingrese la fila del asiento a reservar: ")) - 1 
            columna = int(input("Ingrese la columna del asiento a reservar: ")) - 1

            if fila < 0 or fila >= tamanoSala or columna < 0 or columna >= tamanoSala:
                print("Asiento no válido.")
                return
            
            if asientosDisponibles[fila][columna] == "O":
                asientosDisponibles[fila][columna] = "X"  
                print("Reserva exitosa.")
            else:
                print("El asiento ya está ocupado.")
                return
            
            salaSeleccionada["asientosDisponibles"] = asientosDisponibles
        except Exception as e:
            print("Ingrese solo valores numericos porfavor...")
            print("El error es:", e)
            error(e)
            logerror.append(error(e))
    except Exception as e:
        print("No hay salas disponibles actualmente, reiniciando programa...")
        print("El error es:", e)
        error(e)
        logerror.append(error(e))

def ver_reportes(salas):
    try:
        print("\nReportes:")
        print("Salas existentes y sus respectivos datos:")
        for sala in salas:
            print("Nombre:", sala["nombre"])  
            print("Tamaño:", sala["tamano"], "x", sala["tamano"])  
            print("Película:", sala["pelicula"]) 
            print("Fecha y Hora:", sala["fechaHora"])  
            print("Descripción:", sala["descripcion"])  
            print("\n")  

        print("Películas existentes:")
        peliculas = set(sala["pelicula"] for sala in salas)
        for pelicula in peliculas:  
            print(pelicula)  

        print("Cantidad de puestos vacíos por sala:")
        for sala in salas:
            tamanoSala = sala["tamano"]
            asientosDisponibles = sala["asientosDisponibles"]  
            vacios = sum(row.count("O") for row in asientosDisponibles)  
            print(sala["nombre"] + ":", vacios, "asientos vacíos")  
    except Exception as e:
        print("El error es:", e)
        error(e)
        logerror.append(error(e))

def gestionar_empleados(opcion):
    try:
        while True:
            print("1. Crear empleado.")
            print("2. Buscar empleado.")
            print("3. Eliminar empleado.")
            print("4. Modificar empleado.")
            print("5. Consultar empleados.")
            print("6. Regresar al menú principal.")

            opcion = int(input("Ingrese el numero de la opcion a la cual desea ingresar: "))

            if opcion == 1:
                nombre = input("Ingrese el nombre del empleado: ")
                correo = input("Ingrese el correo electrónico del empleado: ")
                cedula = int(input("Ingrese la cédula del empleado: "))
                direccion = input("Ingrese la dirección del empleado: ")
                fecha_contratacion = input("Ingrese la fecha de contratación del empleado: ")
                cargo = input("Ingrese el cargo del empleado: ")
                estatus = input("Ingrese el estatus del empleado (activo o inactivo): ")
                print("Se ha añadido al empleado", nombre, "a la lista.")

                empleado = {
                    "nombre": nombre,
                    "correo": correo,
                    "cedula": cedula,
                    "direccion": direccion,
                    "fecha_contratacion": fecha_contratacion,
                    "cargo": cargo,
                    "estatus": estatus
                }
                empleados.append(empleado)
            elif opcion == 2:
                cedula = input("Ingrese la cédula del empleado que desea buscar: ")
                encontrado = False
                for empleado in empleados:
                    if empleado["cedula"] == cedula:
                        encontrado = True
                        print("Información del empleado encontrado:")
                        print(f"Nombre: {empleado['nombre']}")
                        print(f"Correo: {empleado['correo']}")
                        print(f"Cédula: {empleado['cedula']}")
                        print(f"Dirección: {empleado['direccion']}")
                        print(f"Fecha de Contratación: {empleado['fecha_contratacion']}")
                        print(f"Cargo: {empleado['cargo']}")
                        print(f"Estatus: {empleado['estatus']}")
                        break

                if not encontrado:
                    print("No se encontró ningún empleado con esa cédula.")
            elif opcion == 3:
                cedula = input("Ingrese la cédula del empleado que desea eliminar: ")

                encontrado = False
                for empleado in empleados:
                    if empleado["cedula"] == cedula:
                        encontrado = True
                        empleados.remove(empleado)
                        print("El empleado fue eliminado")
                        break

                if not encontrado:
                    print("No se encontró ningún empleado con esa cédula.")

            elif opcion == 4:
                cedula = int(input("Ingrese la cédula del empleado que desea modificar: "))

                encontrado = False
                for empleado in empleados:
                    if empleado["cedula"] == cedula:
                        encontrado = True
                        print("Ingrese los nuevos datos del empleado:")
                        nuevo_nombre = input(f"Nombre ({empleado['nombre']}): ")
                        nuevo_correo = input(f"Correo ({empleado['correo']}): ")
                        nueva_direccion = input(f"Dirección ({empleado['direccion']}): ")
                        nuevo_cargo = input(f"Cargo ({empleado['cargo']}): ")
                        nuevo_estatus = input(f"Estatus ({empleado['estatus']}): ")
                        empleado["nombre"] = nuevo_nombre if nuevo_nombre else empleado["nombre"]
                        empleado["correo"] = nuevo_correo if nuevo_correo else empleado["correo"]
                        empleado["direccion"] = nueva_direccion if nueva_direccion else empleado["direccion"]
                        empleado["cargo"] = nuevo_cargo if nuevo_cargo else empleado["cargo"]
                        empleado["estatus"] = nuevo_estatus if nuevo_estatus else empleado["estatus"]
                        print("El perfil del empleado ha sido actualizado.")
                        break
                if not encontrado:
                    print("No se encontró ningún empleado con esa cédula.")
            elif opcion == 5:
                if empleados:
                    print("Lista de empleados:")
                    for empleado in empleados:
                        print(f"Nombre: {empleado['nombre']}")
                        print(f"Correo: {empleado['correo']}")
                        print(f"Cédula: {empleado['cedula']}")
                        print(f"Dirección: {empleado['direccion']}")
                        print(f"Fecha de Contratación: {empleado['fecha_contratacion']}")
                        print(f"Cargo: {empleado['cargo']}")
                        print(f"Estatus: {empleado['estatus']}")
                else:
                    print("No hay empleados registrados.")

            elif opcion == 6:
                print("regresando al menú...")
                break
    except Exception as e:
        print("error, regresando al menú principal...")
        print("el error es:", e)
        error(e)
        logerror.append(error(e))

def gestion_pagos_facturas(opcion2):
    pagos = []
    try:
        while True:
            print("1. Crear un nuevo pago")
            print("2. Modificar un pago existente")
            print("3. Eliminar un pago existente")
            print("4. Consultar información de un pago")
            print("5. Listar todos los pagos")
            print("6. Generar factura por reservación")
            print("7. Salir")

            opcion2 = input("Ingrese el número de la opción deseada: ")

            if opcion2 == "1":
                nombreyapellido = input("Ingrese el nombre y apellido del cliente: ")
                cipago = int(input("Introduzca la cedula del cliente: "))
                correoc = input("Ingrese el correo del cliente: ")
                peliculac = input("Ingrese la pelicula que vera el cliente: ")
                salac = input("Ingrese la sala en la que ingresara el cliente: ")
                cantidadasientos = input("Ingresa la cantidad de asientos reservados: ")
                ubicacionasientos = input("Ingrese la ubicacion de los asientos: ")
                fechapago = input("Ingrese la fecha del pago: ")
                formapago = input("Ingrese la forma del pago: ")
                print("Se ha registrado el pago del empleado con la cedula:", cipago)

                clientespagos = {
                    "Nombre y apellido del cliente": nombreyapellido,
                    "Cedula del cliente": cipago,
                    "Correo del cliente": correoc,
                    "Pelicula": peliculac,
                    "Sala": salac,
                    "Cantidad de asientos": cantidadasientos,
                    "Ubicacion de los asientos": ubicacionasientos,
                    "Fecha del pago": fechapago,
                    "Forma del pago": formapago
                }

                pagos.append(clientespagos)

            elif opcion2 == "2":
                cipago = int(input("introduzca la cedula del cliente al cual quiere modificar su pago: "))
                for clientespagos in pagos:
                    if clientespagos["Cedula del cliente"] == cipago:
                        nombreyapellido_nuevo = input(f"Nombre y apellido del cliente: ({clientespagos['Nombre y apellido del cliente']}): ")
                        nueva_cipago = input(f"Cedula del cliente: ({clientespagos['Cedula del cliente']}): ")
                        correoc_n = input(f"Correo del cliente: ({clientespagos['Correo del cliente']}): ")
                        peliculac_n = input(f"Pelicula: ({clientespagos['Pelicula']}): ")
                        salac_n = input(f"Sala: ({clientespagos['Sala']}): ")
                        cantidadasientos_n = input(f"Cantidad de asientos: ({clientespagos['Cantidad de asientos']}): ")
                        ubicacionasientos_n = input(f"Ubicacion de los asientos: ({clientespagos['Ubicacion de los asientos']}): ")
                        fechapago_n = input(f"Fecha del pago: ({clientespagos['Fecha del pago']}): ")
                        formapago_n = input(f"Forma del pago: ({clientespagos['Forma del pago']}): ")

                        clientespagos["Nombre y apellido del cliente"] = nombreyapellido_nuevo if nombreyapellido_nuevo else clientespagos["Nombre y apellido del cliente"]
                        clientespagos["Cedula del cliente"] = nueva_cipago if nueva_cipago else clientespagos["Cedula del cliente"]
                        clientespagos["Corrreo del cliente"] = correoc_n if correoc_n else clientespagos["Correo del cliente"]
                        clientespagos["Pelicula"] = peliculac_n if peliculac_n else clientespagos["Pelicula"]
                        clientespagos["Sala"] = salac_n if salac_n else clientespagos["Sala"]
                        clientespagos["Cantidad de asientos"] = cantidadasientos_n if cantidadasientos_n else clientespagos["Cantidad de asientos"]
                        clientespagos["Ubicacion de los asientos"] = ubicacionasientos_n if ubicacionasientos_n else clientespagos["Ubicacion de los asientos"]
                        clientespagos["Fecha del pago"] = fechapago_n if fechapago_n else clientespagos["Fecha del pago"]
                        clientespagos["Forma del pago"] = formapago_n if formapago_n else clientespagos["Forma del pago"]
                        print("Se ha registrado el pago.")
                        break
            elif opcion2 == "3":
                ci_pago = int(input("Ingrese el numero del pago que desea eliminar: "))
                ci_pago = ci_pago - 1
                for ci_pago in pagos:
                    print("iniciando proceso...")
                    pagos.remove(clientespagos)
                    print("El pago del empleado fue eliminada")
                    break

            elif opcion2 == "4":
                ci_pago_2 = input("Ingrese el numero del pago que desea consultar: ")
                ci_pago_2 = ci_pago_2 - 1
                for ci_pago_2 in pagos:
                        print(f"Nombre y apellido del cliente: ({clientespagos['Nombre y apellido del cliente']}): ")
                        print(f"Cedula del cliente: ({clientespagos['Cedula del cliente']}): ")
                        print(f"Correo del cliente: ({clientespagos['Correo del cliente']}): ")
                        print(f"Pelicula: ({clientespagos['Pelicula']}): ")
                        print(f"Sala: ({clientespagos['Sala']}): ")
                        print(f"Cantidad de asientos: ({clientespagos['Cantidad de asientos']}): ")
                        print(f"Ubicacion de los asientos: ({clientespagos['Ubicacion de los asientos']}): ")
                        print(f"Fecha del pago: ({clientespagos['Fecha del pago']}): ")
                        print(f"Forma del pago: ({clientespagos['Forma del pago']}): ")
            elif opcion2 == "5":
                print("La lista de pagos registrados son:")
                print(pagos)

            elif opcion2 == "6":
                facturas = int(input("Ingrese el numero del pago del cual desea generar la factura: "))
                facturas = facturas - 1
                for facturas in pagos:
                    print(clientespagos)
                    
            elif opcion2 == "7":
                break
    except Exception as e:
        print("El error es:", e)
        error(e)
        logerror.append(error(e))
        
def error(e):
    error = {"hora:": datetime.datetime.now(),
             "descripcion":e,
             }
    return error

def main():

    while True:
        print('<------------------------------------>')
        print("\nMenú de Opciones:")
        print("1. Configurar Salas.")  
        print("2. Reservar Asientos.")  
        print("3. Ver Reportes.")
        print("4. Gestionar Empleados.")
        print("5. Gestion de pagos y facturas.")
        print("6. logerrores.")
        print("7. Salir.") 
        print('<------------------------------------>')
        opcion = input("Seleccione una opción: ")
        if opcion == "1": 
            salas = configurar_salas()  
        elif opcion == "2":
            reservar_asientos(salas)  
        elif opcion == "3":
            ver_reportes(salas)  
        elif opcion == "4":
            gestionar_empleados(opcion)
        elif opcion == "5":
            gestion_pagos_facturas(opcion)
        elif opcion == "6":
            print(logerror)
        elif opcion == "7":
            break  
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
main()




