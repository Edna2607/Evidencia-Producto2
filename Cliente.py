from Usuario import Usuario

class Cliente(Usuario):
    def __init__(self, id, nombre, correo, password, rol):
        super().__init__(id, nombre, correo, password)
        self._rol = rol
        self._pais = None
        self._dias = None
        self._personas = None
        self._fecha1 = None
        self._fecha2 = None

    @property
    def rol(self):
        return self._rol

    def registrar_viaje(self, pais, dias, personas, fecha1, fecha2):
        self._pais = pais
        self._dias = dias
        self._personas = personas
        self._fecha1 = fecha1
        self._fecha2 = fecha2

    def mostrar_viaje(self):
        print(f"Pais: {self._pais}")
        print(f"Días: {self._dias}")
        print(f"Personas: {self._personas}")
        print(f"Fecha de ida: {self._fecha1}")
        print(f"Fecha de regreso: {self._fecha2}")

