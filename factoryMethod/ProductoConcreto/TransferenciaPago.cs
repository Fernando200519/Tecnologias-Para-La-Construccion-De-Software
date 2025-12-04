using producto;
namespace ProductoConcreto
{
    public class TransferenciaPago : IPago
    {
        public void procesarPago(decimal monto)
        {
            Console.WriteLine("Procesando pago con transferencia");
        }

        public bool validarPago()
        {
            System.Console.WriteLine("Validando transferencia..");
            return true;
        }

    }
}