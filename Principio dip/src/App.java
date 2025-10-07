import mal_ejemplo.ServicioNoti;
import buen_ejemplo.Email;
import buen_ejemplo.Notificador;
import buen_ejemplo.ServicioNotificador;
import buen_ejemplo.Sms;
import buen_ejemplo.WhatsApp;


public class App {
    public static void main(String[] args) throws Exception {
        
        ServicioNoti servicioNoti = new ServicioNoti();
        servicioNoti.enviar("Hola mundo");

        Notificador email = new Email();
        Notificador sms = new Sms();
        Notificador whatsapp = new WhatsApp();

        ServicioNotificador Servicioemail = new ServicioNotificador(email);
        ServicioNotificador Serviciosms = new ServicioNotificador(sms);
        ServicioNotificador Serviciowhatsapp = new ServicioNotificador(whatsapp);

        Servicioemail.notificar("Hola mundo vía email");
        Serviciosms.notificar("Hola mundo vía sms");
        Serviciowhatsapp.notificar("Hola mundo vía whatsapp");

        

        
    }
}
