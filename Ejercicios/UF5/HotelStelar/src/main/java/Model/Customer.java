package Model;

public class Customer extends Persona {
    private int cantidadPersonas;
    private String[] requisitosHabitacion;

    public Customer(String DNI, int cantidadPersonas, String[] requisitosHabitacion) {
        super(DNI);
        this.cantidadPersonas = cantidadPersonas;
        this.requisitosHabitacion = requisitosHabitacion;
    }

    public int getCantidadPersonas() {
        return cantidadPersonas;
    }

    public String[] getRequisitosHabitacion() {
        return requisitosHabitacion;
    }
}
