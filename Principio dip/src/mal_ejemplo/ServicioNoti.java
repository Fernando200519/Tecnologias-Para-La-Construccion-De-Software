package mal_ejemplo;

public class ServicioNoti {
    private mal_ejemplo.correo correo = new correo();

    public void enviar(String mensaje) {
        correo.enviar(mensaje);
    }
}
