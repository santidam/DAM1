package Model;

import java.util.Arrays;
import java.util.HashMap;

import java.util.HashSet;
import java.util.Set;

public class Habitacion  {

    private String numero;
    private int capacidad;
    private HashSet<String> serveis;
    private String estado;
    private Customer customer;



    public Habitacion(String numero, int capacidad, HashSet<String> serveis) {
        this.numero = numero;
        this.capacidad = capacidad;
        this.serveis = serveis;
        this.estado = "clean";
        this.customer = null;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }


    public String getNumero() {
        return numero;
    }

    public int getCapacidad() {
        return capacidad;
    }

    public HashSet<String> getServeis() {
        return serveis;
    }

    public String getEstado() {
        return estado;
    }

    @Override
    public String toString() {
        if (customer==null){
            return "ROOM "+ numero+ estado.toUpperCase();
        }
        return "ROOM "+ numero+ "CUSTOMER:" +customer.getDNI()+"("+customer.getCantidadPersonas()+")";
    }
}
