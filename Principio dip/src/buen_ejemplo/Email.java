package buen_ejemplo;

public class Email implements Notificador {
    @Override
    public void enviar(String mensaje) {
        System.out.println("Enviando correo " + mensaje);
    }
    
}
