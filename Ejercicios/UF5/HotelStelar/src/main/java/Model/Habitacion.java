package Model;

import java.util.*;

public class Habitacion implements Comparable  {

    private String numero;
    private int capacidad;
    private Set<String> servicios;
    private String estado;
    private Customer customer;
    private HashMap<String,Worker> peticiones;
    public Habitacion(String numero, int capacidad, String[] servicios) {
        this.numero = numero;
        this.capacidad = capacidad;
        this.servicios = new HashSet<>(Arrays.asList(servicios));
        this.estado = "clean";
        this.customer = null;
        this.peticiones = new HashMap<>();
    }
    //    public String toStringWrite(){
//        return nombre+";"+tipo+";"+precio+";"+disponibilidad+";"+ventas;
//    }

    public String getNumero() {
        return numero;
    }

    public String getEstado() {
        return estado;
    }

    public int getCapacidad() {
        return capacidad;
    }

    public Set<String> getServicios() {
        return servicios;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }
    public void addPeticion(String peticion, Worker w){
        peticiones.put(peticion,w);
    }
    public void removePeticion(String peticion){
        peticiones.remove(peticion);
    }
    public void clearPeticiones(){
        peticiones.clear();
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

    public HashMap<String, Worker> getPeticiones() {
        return peticiones;
    }

    @Override
    public String toString() {
        return "Tipo de plato: " +
                "\n"  + " - Precio: "  + "€ - Cantidad disponible: " ;
    }

    @Override
    public int compareTo(Object o) {
        Habitacion h = (Habitacion) o;
        return capacidad-h.getCapacidad();
    }
}
