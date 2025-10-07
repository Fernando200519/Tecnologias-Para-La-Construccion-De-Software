namespace TiposDePolimosfismo.Figuras
{
    public class Circulo : Figura
    {
        private double radio;

        public Circulo(double radio)
        {
            this.radio = radio;
        }

        public override double calcularArea()
        {
            return Math.PI * radio * radio;
        }

        public override void dibujar()
        {
            Console.WriteLine("Dibujando un círculo con radio: " + radio);
        }
    }
}