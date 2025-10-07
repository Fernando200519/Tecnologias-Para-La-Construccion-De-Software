package buen_ejemplo;

public class ServicioNotificador {
    private Notificador notificador;

    public ServicioNotificador(Notificador notificador) {
        this.notificador = notificador;
    }

    public void notificar(String mensaje) {
        notificador.enviar(mensaje);
    }
    
}
