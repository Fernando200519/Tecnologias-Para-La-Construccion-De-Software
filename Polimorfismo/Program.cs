using System;
using TiposDePolimosfismo.Figuras;
using TiposDePolimosfismo.Unidades;
using TiposDePolimosfismo.Genericos;
using TiposDePolimosfismo.Utilidades;

class Program
{
    public static void Main(string[] args)
    {
        List<Figura> figuras = new List<Figura>()
        {
            new Circulo(5),
            new Rectangulo(4,6)
        };

        foreach (var f in figuras)
        {
            f.dibujar();
            Console.WriteLine($"Area: {f.calcularArea()}");
        }

        Caja<string> caja1 = new Caja<string>();
        caja1.Guardar("Hola Mundo");
        Console.WriteLine($"Contenido de la caja: {caja1.Abrir()}");

        Caja<int> caja2 = new Caja<int> ();
        caja2.Guardar(123);
        Console.WriteLine($"Contenido de la caja: {caja2.Abrir()}");

        Calculadora calc = new Calculadora();
        Console.WriteLine($"Suma de Decimales: {calc.sumar(5, 10)}");
        Console.WriteLine($"Suma de Decimales: {calc.sumar(5.5, 10.3)}");

        Metro m = 10;
        double d = (double)m;
        Console.WriteLine($"Metros: {m}, Decimales: {d}");
    }
}