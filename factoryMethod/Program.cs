using Factory;
using Producto;

class Program
{
    static void Main()
    {
        ProcesarPago(TipoPago.TarjetaCreditoPago(100.50));
        ProcesarPago(TipoPago.PayPal(10.50));
        ProcesarPago(TipoPago.TransferenciaPago(1.50));
    }

    static void ProcesarPago(TipoPago tipo, decimal monto)
    {
        IPago =  tipo.CrearPago(monto);
    }

}