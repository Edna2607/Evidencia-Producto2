from Usuario import Usuario

class Agencia(Usuario):
    def __init__(self, id, nombre, correo, password, rol):
        super().__init__(id, nombre, correo, password)
        self._rol = rol
        self.clientes = []  # Lista para almacenar clientes
        self.paquetes_de_viaje = []  # Lista para almacenar paquetes de viaje

    def mostrar_cliente_y_viaje(self):
        print("---- Información de Clientes y Paquetes de Viaje ----")
        for cliente in self.clientes:
            cliente.imprimir_info()
            precio_total_cliente = 0  # Inicializa el precio total del cliente
            for paquete in self.paquetes_de_viaje:
                if cliente.nombre == paquete["nombre_cliente"]:
                    print(
                        f"Paquete de Viaje: Lugar: {paquete['lugar']}, "
                        f"Días: {paquete['dias']}, "
                        f"Precio por persona: {paquete['precio']}, "
                        f"Personas: {paquete['personas']}, "
                        f"Precio Total: {paquete['precio_total']}")
                    precio_total_cliente += paquete['precio_total']  # Agrega al precio total del cliente
            print(f"Precio Total para {cliente.nombre}: {precio_total_cliente}")  # Muestra el precio total del cliente
            print("-----------------------------------------------------")


    def registrar_viaje(self, pais, dias, personas, fecha1, fecha2):
        self._pais = pais
        self._dias = dias
        self._personas = personas
        self._fecha1 = fecha1
        self._fecha2 = fecha2

    def aprobar_pedido(self):
        print(f"La Agencia {self._nombre} ha aprobado un viaje.")

    def registrar_viaje(self):
        self._pais = input(f"Ingrese el Pais de Destino: ")
        self._dias = input(f"Ingrese los días: ")
        self._personas = input(f"Ingrese la cantidad de personas: ")
        self._fecha1 = input(f"Ingrese la fecha de ida: ")
        self._fecha2 = input(f"Ingrese la fecha de regreso: ")

    def mostrar_viaje(self):
        print(f"Pais: {self._pais} ")
        print(f"Días: {self._dias}")
        print(f"Personas: {self._personas}")
        print(f"Fecha de ida: {self._fecha1}")
        print(f"Fecha de regreso: {self._fecha2}")



