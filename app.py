def crear_sala(nombre, tamaño, pelicula, fecha_hora, descripcion):
    asientos = [[False] * tamaño for _ in range(tamaño)]
    nueva_sala = {
        "nombre": nombre,
        "tamaño": tamaño,
        "pelicula": pelicula,
        "fecha_hora": fecha_hora,
        "descripcion": descripcion,
        "asientos": asientos
    }
    return nueva_sala


def mostrar_info_sala(sala):
    print('Información de la sala:')
    print(f"Sala: {sala['nombre']}")
    print(f"Película: {sala['pelicula']}")
    print(f"Fecha y Hora: {sala['fecha_hora']}")
    print(f"Descripción: {sala['descripcion']}")
    print(f"Tamaño de la sala: {sala['tamaño']}x{sala['tamaño']}")


def mostrar_asientos_disponibles(sala):
    print("Matriz de asientos:")
    for fila in sala['asientos']:
        print(" ".join(["O" if disponible else "X" for disponible in fila]))


def reservar_asiento(sala, fila, columna):
    if 1 <= fila <= sala['tamaño'] and 1 <= columna <= sala['tamaño']:
        sala['asientos'][fila - 1][columna - 1] = True
        return True
    else:
        return False


def mostrar_salas(salas):
    for sala in salas:
        mostrar_info_sala(sala)
        


def mostrar_peliculas(salas):
    peliculas = set()
    for sala in salas:
        peliculas.add(sala['pelicula'])
    print("Películas disponibles:")
    for pelicula in peliculas:
        print(pelicula)


def reporte_puestos_vacios(salas):
    for sala in salas:
        puestos_vacios = sum([fila.count(False) for fila in sala['asientos']])
        print(f"En la sala {sala['nombre']} hay {puestos_vacios} puestos vacíos.")

def crear_empleado(nombre,apellido,email,cedula,direccion,fecha_de_contratacion,cargo,status):
    new_empleado = {
        nombre,
        apellido,
        email,
        cedula,
        direccion,
        fecha_de_contratacion,
        cargo,
        status
    }
    return new_empleado
def eliminar_empleado(empleados,cedula):
    new_empleados = []
    for empleado in empleados:
        if cedula != empleado['cedula']:
            new_empleados.append(empleado)
    empleados = new_empleados

def listar_empleados(empleados):
    for empleado in empleados:
        print('Nombre:', empleado['nombre'])
        print('apellido:', empleado['apellido'])
        print('email:', empleado['email'])
        print('cedula:', empleado['cedula'])
        print('direccion:', empleado['direccion'])
        print('fecha_de_contratacion:', empleado['fecha_de_contratacion'])
        print('cargo:', empleado['cargo'])
        print('status:', empleado['status'])
def menu():
    salas = []
    empleados = []

    while True:
        print("\nMenú de Opciones:")
        print("1. Agregar Sala")
        print("2. Mostrar Salas")
        print("3. Mostrar Películas")
        print("4. Reservar Asiento")
        print("5. Reporte de Puestos Vacíos")
        print("6. Agragar empleado")
        print("7. Mostrar informacion de empleado")
        print("8. Modificar informacion de empleado")
        print("9. Eliminar informacion de empleado")
        print("10. Eliminar informacion de empleado")

        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la sala: ")
            tamaño = int(input("Tamaño de la sala (n x n): "))
            pelicula = input("Película a proyectar: ")
            fecha_hora = input("Fecha y hora: ")
            descripcion = input("Descripción de la sala: ")
            sala = crear_sala(nombre, tamaño, pelicula, fecha_hora, descripcion)
            salas.append(sala)

        elif opcion == "2":
            mostrar_salas(salas)

        elif opcion == "3":
            mostrar_peliculas(salas)

        elif opcion == "4":
            sala_seleccionada = input("Nombre de la sala a reservar: ")
            sala = next((s for s in salas if s['nombre'] == sala_seleccionada), None)
            if sala:
                mostrar_asientos_disponibles(sala)
                fila = int(input("Ingrese la fila del asiento a reservar: "))
                columna = int(input("Ingrese la columna del asiento a reservar: "))
                if reservar_asiento(sala, fila, columna):
                    print("Reserva exitosa.")
                else:
                    print("Este asiento ya está reservado.")
            else:
                print("Sala no encontrada.")

        elif opcion == "5":
            reporte_puestos_vacios(salas)

        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, elija una opción válida.")


if __name__ == "__main__":
    menu()