using Producto;
using ProductoConcreto;

namespace Factoty
{
    public static class PagoFactory
    {
        public static IPago crearPago(TipoPago tipoPago)
        {
            return tipoPago switch
            {
                tipoPago.TarjetaCreditoPago => new TarjetaCreditoPago(),
                tipoPago.PayPal => new PayPalPago(),
                tipoPago.transferencia => new TransferenciaPago()
            };
        }
    }
}