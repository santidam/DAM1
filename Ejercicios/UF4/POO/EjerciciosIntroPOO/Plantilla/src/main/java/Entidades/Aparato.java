package Entidades;

public class Aparato {

    private String propietario;
    private String descripcion;
    private double potencia;
    private boolean interuptor;

    public Aparato(String propietario,String descripcion, double potencia) {
        this.descripcion = descripcion;
        this.potencia = potencia;
        this.interuptor = false;
        this.propietario = propietario;
    }

    public String getPropietario() {
        return propietario;
    }

    public void setInteruptor(boolean interuptor) {
        this.interuptor = interuptor;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public double getPotencia() {
        return potencia;
    }

    public boolean isInteruptor() {
        return interuptor;
    }

    public String toStringWrite(){

        return this.propietario+";"+this.descripcion+";"+this.potencia+";"+this.interuptor;
    }
    @Override
    public String toString() {
        return "Aparato: "+ descripcion +
                "\nPotencia: " + potencia +
                "\nInteruptor: " + interuptor;
    }
}
