using system;

namespace ProductoConcreto
{
    public class PayPalPago : IPago
    {
        public void ProcesarPago(decimal monto)
        {
            Console.WriteLine($"Procesando pago con PayPay");
        }

        public bool validarPago()
        {
            Console.WriteLine("Validando cuenta PayPay..");
            return true;
        }
    }
}