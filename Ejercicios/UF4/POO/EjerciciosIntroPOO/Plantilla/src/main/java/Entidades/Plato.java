package Entidades;

import java.util.ArrayList;

public class Plato {

    private String nombre;
    private String tipo;

    private double precio;

    private int disponibilidad;
    private int ventas;



    public Plato(String nombre,String tipo,double precio) {
        this.nombre = nombre;
        this.tipo = tipo;
        this.precio = precio;
        this.disponibilidad = 0;
        this.ventas = 0;
    }

    public int getVentas() {
        return ventas;
    }
    public void sumarVentas(int num){
        ventas = ventas + num;
    }

    public void setVentas(int ventas) {
        this.ventas = ventas;
    }

    public String getNombre() {
        return nombre.toLowerCase();
    }

    public String toStringWrite(){
        return nombre+";"+tipo+";"+precio+";"+disponibilidad+";"+ventas;
    }

    public int getDisponibilidad() {
        return disponibilidad;
    }

    public void setDisponibilidad(int disponibilidad) {
        this.disponibilidad = disponibilidad;
    }

    public void sumarDisponibilidad(int num){
        disponibilidad+= num;
    }
    public void restarDispoonibilidad(int num){
        disponibilidad-= num;
    }

    public String getTipo() {
        return tipo;
    }

    public double getPrecio() {
        return precio;
    }

    @Override
    public String toString() {
        return "Tipo de plato: " + tipo +
                "\n" + nombre + " - Precio: " + precio + "€ - Cantidad disponible: " + disponibilidad;
    }

}
