1. Módulo de Configuración de Salas: Desarrolle un módulo que permita a los administradores del sistema configurar las salas de cine. Los administradores podrán definir el tamaño de cada sala(nxn), película a proyectar, fecha y hora, descripción de la salsa. Estas configuraciones de sala se guardarán en una lista en Python para su posterior gestión y programación de funciones. Este módulo también debe permitir modificar una sala seleccionada.

2. Módulo de Reservación de asientos: Desarrolle un módulo de reservación de asientos cuyo proceso es el siguiente: Primero permitirá mostrar una lista de salas existentes junto a la película, hora y fecha. El usuario seleccionará una sala y se mostrará una matriz con los asientos existentes disponibles y no disponibles. Una vez que se muestre esta matriz de asientos existentes, el usuario introducirá en pantalla la posición en fila y columna del siento a reservar. 

3. Módulo de Menú de opciones: Este módulo permitirá mostrar un menú de opciones a través del cual se acceder a los módulos antes desarrollados en los demás módulos

4. Módulo de reportes: Este módulo debe relistar lo siguiente:

a. Salas existentes y sus respectivos datos.
b. Películasexistentes.
c. Cantidad de puestos vacíos por sala ✅

5. Log de Errores: Mediante el uso de excepciones, el programa debe registrar todos los errores ocurrido durante su ejecución, y listarlos siempre que el usuario lo necesite. El log debe contener: hora en que ocurrió el error, tipo de error, función donde ocurrió el error, descripción del error.

6. Gestión de empleados: El programa deberá permitir la gestión de empleados(crear, buscar, eliminar, modificar, consultar) de la cadena de cines. Cada empleado debe tener los siguientes campos: nombre, apellido, correo electrónico, cédula, dirección, fecha de contratación(dd/mm/yyyy), cargo, estatus(activo, inactivo).

7. Gestión de Pagos y Facturas: Este módulo debe permitir gestionar(crear, modificar, eliminar, consultar y listar) pagos y generar facturas por cada reservación. Cada pago debe contener: nombre y apellido del cliente, cédula del cliente, correo del cliente,película, sala(Validar que la sala exista), cantidad de asientos y su ubicación, fecha de pago, forma de pago. Al momento de agregar un pago, se debe validar que los asientos seleccionados deben estar marcados previamente