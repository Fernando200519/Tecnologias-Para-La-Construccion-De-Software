namespace TiposDePolimosfismo.Genericos
{
    public class Caja<T>
    {
        private T contenido;

        public void Guardar(T item)
        {
            contenido = item;
        }

        public T Abrir()
        {
            return contenido;
        }
    }
}