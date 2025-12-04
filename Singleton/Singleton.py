from datetime import datetime, date

class Logger:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance._logs = []  # inicializado en la única instancia
        return cls.__instance
    
    def log(self, mensaje: str) -> None:
        self._logs.append(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {mensaje}")

    def show_logs(self) -> list[str]:
        return self._logs


class Usuario:
    def __init__(self, usuario_id: str, nombre: str) -> None:
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.pedidos: list["Pedido"] = []

    def registrar(self) -> None:
        logger = Logger()
        logger.log(f"El usuario {self.usuario_id} se registró")

    def agregarPedido(self, pedido: "Pedido") -> None:
        self.pedidos.append(pedido)
        logger = Logger()
        logger.log(f"El pedido {pedido.id} se agregó")

    def get_pedidos(self) -> list["Pedido"]:
        return self.pedidos


class Pedido:
    def __init__(self, pedido_id: int, fecha: date, precio: float) -> None:
        self.id = pedido_id
        self.fecha = fecha
        self.precio = precio
        self.estado = "Pendiente"
    
    def procesar(self) -> None:
        logger = Logger()
        logger.log(f"El pedido {self.id} se procesó")
        self.estado = "Procesado"

    def cancelar(self) -> None:
        logger = Logger()
        logger.log(f"El pedido {self.id} se canceló")
        self.estado = "Cancelado"
    
    def mostrarDetalles(self) -> str:
        return f"Pedido: {self.id} | fecha: {self.fecha} | precio: {self.precio} | estado: {self.estado}"
    

if __name__ == "__main__":
    user = Usuario("1", "Fernandito")
    user.registrar()

    p1 = Pedido(1, date(2022, 1, 1), 100)
    user.agregarPedido(p1)
    p1.procesar()

    p2 = Pedido(2, date(2022, 1, 2), 200)
    user.agregarPedido(p2)
    p2.cancelar()

    print(f"Pedidos del usuario {user.nombre}:")
    for pedido in user.get_pedidos():
        print(pedido.mostrarDetalles())

    logger = Logger()

    print("\nRegistros globales del logger (singleton):")
    for log in logger.show_logs():
        print(log)
