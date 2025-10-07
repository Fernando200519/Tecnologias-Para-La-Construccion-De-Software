public class Notificacion {
    private String cliente;
    private String mensaje;

    public Notificacion(String cliente, String mensaje) {
        this.cliente = cliente;
        this.mensaje = mensaje;
    }

    public void enviarMensaje() {
        System.out.println(cliente + " " + mensaje);
    }
}
