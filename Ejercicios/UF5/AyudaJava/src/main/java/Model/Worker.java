package Model;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Worker extends Persona{
    private String nombre;
    private HashSet<String> habilidad;
    private String estado;

    public Worker(String DNI, String nombre, HashSet<String> habilidad) {
        super(DNI);
        this.nombre = nombre;
        this.habilidad = habilidad;
        this.estado = "available";
    }

    public String getNombre() {
        return nombre;
    }

    public HashSet<String> getHabilidad() {
        return habilidad;
    }


    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }

    @Override
    public String toString() {
            return "WORKER "+ getDNI()+" "+ nombre +" "+estado.toUpperCase();
    }
}
