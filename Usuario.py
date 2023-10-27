class Usuario:
    def __init__(self, id, nombre, correo, password):
        self._id = id
        self._nombre = nombre
        self._correo = correo
        self._password = password

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    def iniciar_sesion(self, correo, password):
        return self._correo == correo and self._password == password

    def registrar_usuario(self):
        self._id = input(f"Ingrese el id del usuario: ")
        self._nombre = input(f"Ingrese el nombre del usuario: ")
        self._correo = input(f"Ingrese el correo del usuario: ")
        self._password = input(f"Ingrese la contraseña del usuario: ")

    def imprimir_info(self):
        print(f"ID: {self._id}, Cliente: {self._nombre}, Correo: {self._correo}")


