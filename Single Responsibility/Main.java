public class Main {
    public static void main(String[] args) {
        SistemaPedidos pedidos = new SistemaPedidos("Elias", "Espresso");
        MaquinaCafe maquina = new MaquinaCafe("Espresso");
        Factura factura = new Factura("Elias", 82.70);
        Notificacion notificacion = new Notificacion("Elias", "Tu pedido esta listo");
    }
}
