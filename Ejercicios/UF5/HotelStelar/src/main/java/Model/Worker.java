package Model;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Worker extends Persona{
    private String nombre;
    private Set<String> habilidad;
    private String estado;

    public Worker(String DNI, String nombre, String[] habilidad) {
        super(DNI);
        this.nombre = nombre;
        this.habilidad = new HashSet<>(Arrays.asList(habilidad));
        this.estado = "available";
    }

    public String getNombre() {
        return nombre;
    }

    public Set<String> getHabilidad() {
        return habilidad;
    }

    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }
}
