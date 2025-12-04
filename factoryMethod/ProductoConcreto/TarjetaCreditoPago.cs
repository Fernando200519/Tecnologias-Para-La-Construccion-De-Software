using system;
using producto;

namespace ProductoConcreto
{
    public class TarjetaCreditoPago: IPago
    {
        public void procesarPago(decimal monto)
        {
            Console.WriteLine("Procesando pago con tarjeta de credito");
        }

        public bool validarPago()
        {
            System.Console.WriteLine("Validando tarjeta de credito..");
            return true;
        }
    }
}