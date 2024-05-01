package Entidades;

public class Placa {

    private double superficie;
    private double precio;
    private double potencia;
    private String propietario;
    public Placa(String propietario, double superficie, double precio, double potencia) {
        this.superficie = superficie;
        this.precio = precio;
        this.potencia = potencia;
        this.propietario = propietario;
    }

    public String toStringWrite(){
        return this.propietario+";"+this.superficie+";"+this.precio+";"+this.potencia;
    }

    public String getPropietario() {
        return propietario;
    }

    public double getPotencia() {
        return potencia;
    }

    public double getSuperficie() {
        return superficie;
    }

    public double getPrecio() {
        return precio;
    }

    @Override
    public String toString() {
        return "superficie: " + superficie +
                "\nPrecio: " + precio +
                "\nPotencia: " + potencia;
    }
}
