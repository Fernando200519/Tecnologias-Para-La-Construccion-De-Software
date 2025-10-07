package buen_ejemplo;

public class WhatsApp implements Notificador {
    @Override
    public void enviar(String mensaje) {
        System.out.println("Enviando whatsapp " + mensaje);
    }
    
}
