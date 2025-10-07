public class MaquinaCafe {
    private String tipoCafe;

    public MaquinaCafe(String tipoCafe) {
        this.tipoCafe = tipoCafe;
    }

    public void prepararCafe(){
        System.out.println("Se prepara un cafe de tipo: " + tipoCafe);
    }
}
