using System.Runtime.CompilerServices;

namespace TiposDePolimosfismo.Unidades
{
    public class Metro
    {
        private double Valor { set; get; }
        public Metro(double valor)
        {
            this.Valor = valor;
        }
        
        public static implicit operator double(Metro m)
        {
            return m.Valor;
        }

        public static implicit operator Metro(double d)
        {
            return new Metro(d);
        }
    }
}