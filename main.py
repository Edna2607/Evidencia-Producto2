from Cliente import Cliente
from Usuario import Usuario
from Agencia import Agencia

usuario = None  # Variable para mantener un registro del usuario

def menu_principal():
    global usuario  # Necesario para acceder a la variable usuario definida fuera de la función
    print("-----AGENCIA DE VIAJES------")
    print("1. Ingresar como Cliente")
    print("2. Ingresar como Agencia")
    print("3. ---Salir---")
    print("--------------------------")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        usuario = Cliente(None, None, None, None, None)  # Crear una instancia de cliente
        menu_cliente()
    elif opcion == "2":
        usuario = Agencia(None, None, None, None, None)  # Crear una instancia de agencia
        menu_agencia()
    elif opcion == "3":
        print("Saliendo del programa.")
    else:
        print("Opción no válida.")

def menu_cliente():
    print("-----Menú Cliente-------")
    print("1. Registro")
    print("2. Iniciar sesión")
    print("3. Viaje")
    print("4. Confirmación de su viaje")
    print("5. Salir")
    print("-------------------------")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        usuario.registrar_usuario()
        menu_cliente()  # Volver al menú del cliente
    elif opcion == "2":
        correo = input("Ingrese su correo: ")
        password = input("Ingrese su contraseña: ")
        if usuario.iniciar_sesion(correo, password):
            print("Inicio de sesión exitoso.")

            # Definir una función lambda para una acción personalizada
            custom_action = lambda: print("Acción personalizada después de iniciar sesión.")

            # Definir un callback para ejecutar la acción personalizada
            def callback():
                custom_action()
                menu_cliente()  # Volver al menú del cliente

            callback()  # Ejecutar el callback
        else:
            print("Inicio de sesión fallido.")
            menu_cliente()  # Volver al menú del cliente
    elif opcion == "3":
        if isinstance(usuario, Cliente):
            # Permite al cliente ingresar valores del viaje
            pais = input("Ingrese el país de destino: ")
            dias = input("Ingrese la cantidad de días: ")
            personas = input("Ingrese la cantidad de personas: ")
            fecha1 = input("Ingrese la fecha de ida: ")
            fecha2 = input("Ingrese la fecha de regreso: ")

            # Llama a la función para registrar el viaje en el propio objeto Cliente
            usuario.registrar_viaje(pais, dias, personas, fecha1, fecha2)
            print("Viaje registrado exitosamente.")

        else:
            print("No puedes elegir un viaje como Agencia.")
        menu_cliente()  # Volver al menú del cliente
    elif opcion == "4":
        print("-----ITINERARIO DE VIAJE------")
        usuario.imprimir_info()
        print("----Descripcion----")
        usuario.mostrar_viaje()
        print("itinerario guardado- Pedir a la agencia su confirmación de viaje")
        print("---------------------------------")
        menu_cliente()  # Volver al menú del cliente
    elif opcion == "5":
        menu_principal()  # Volver al menú principal
    else:
        print("Opción no válida.")
        menu_cliente()  # Volver al menú del cliente

def menu_agencia():
    print("------Menú Agencia--------")
    print("1. Ingresar Clientes")
    print("2. Ingresar Itinerario de Viaje")
    print("3. Mostrar Clientes y su Itinerario")
    print("4. Salir")
    print("-----------------------------")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Solicitar información del cliente
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        correo_cliente = input("Ingrese el correo del cliente: ")
        telefono_cliente = input("Ingrese el teléfono del cliente: ")

        nuevo_cliente = Cliente(None, nombre_cliente, correo_cliente, None, None)
        usuario.clientes.append(nuevo_cliente)  # Agregar el cliente a la lista de clientes

        print("Cliente registrado exitosamente.")
        menu_agencia()  # Volver al menú de la agencia
    elif opcion == "2":
        # Solicitar información de paquetes de viaje
        lugar = input("Ingrese el lugar de viaje: ")
        dias = int(input("Ingrese la cantidad de días: "))
        precio = float(input("Ingrese el precio por persona: "))
        personas = int(input("Ingrese la cantidad de personas: "))

        # Solicitar el nombre del cliente al que se asocia este paquete de viaje
        nombre_cliente_paquete = input("Ingrese el nombre del cliente al que pertenece este paquete: ")

        # Calcular el precio total
        precio_total = precio * personas

        nuevo_paquete = {
            "lugar": lugar,
            "dias": dias,
            "precio": precio,
            "personas": personas,
            "nombre_cliente": nombre_cliente_paquete,  # Asocia el paquete al cliente
            "precio_total": precio_total  # Agrega el precio total
        }
        usuario.paquetes_de_viaje.append(nuevo_paquete)  # Agregar el paquete de viaje a la lista de paquetes de viaje

        print(f"Paquete de viaje registrado exitosamente.")
        print(f"Precio total: {precio_total}")

        menu_agencia()  # Volver al menú de la agencia
    elif opcion == "3":
        # Mostrar información de clientes y paquetes de viaje
        usuario.mostrar_cliente_y_viaje()
        menu_agencia()  # Volver al menú de la agencia
    elif opcion == "4":
        menu_principal()  # Volver al menú principal
    else:
        print("Opción no válida.")
        menu_agencia()  # Volver al menú de la agencia

if __name__ == "__main__":
    while True:
        menu_principal()






