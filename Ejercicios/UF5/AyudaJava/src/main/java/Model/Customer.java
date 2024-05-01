package Model;

import java.util.HashSet;

public class Customer extends Persona {
    private int cantidadPersonas;
    private HashSet<String> requisitosHabitacion;

    public Customer(String DNI, int cantidadPersonas, HashSet<String> requisitosHabitacion) {
        super(DNI);
        this.cantidadPersonas = cantidadPersonas;
        this.requisitosHabitacion = requisitosHabitacion;
    }

    public int getCantidadPersonas() {
        return cantidadPersonas;
    }

    public HashSet<String> getRequisitosHabitacion() {
        return requisitosHabitacion;
    }
}
