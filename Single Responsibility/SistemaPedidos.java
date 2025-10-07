public class SistemaPedidos {
    private String cliente;
    private String cafe;

    public SistemaPedidos(String cliente, String cafe){
        this.cliente = cliente;
        this.cafe = cafe;
    }

    public String getCliente() {
        return cliente;
    }

    public String getCafe() {
        return cafe;
    }

    public void setCliente(String cliente) {
        this.cliente = cliente;
    }

}