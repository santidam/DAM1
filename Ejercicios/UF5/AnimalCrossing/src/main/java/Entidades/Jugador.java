package Entidades;

import java.util.ArrayList;
import Enum.*;

public class Jugador {

    private String nombre;
    private int calacoin;
    private int nivel;
    private  ArrayList<Herramienta> listHerramientas;
    private String escenario;


    public Jugador(String nombre) {
        this.nombre = nombre;
        this.calacoin = 100;
        this.nivel = 1;
        this.listHerramientas = new ArrayList<>();
        this.escenario = String.valueOf(Escenario.SECRETARIA);
    }
//
//    public String toStringWrite(){
//        return nombre+";"+tipo+";"+precio+";"+disponibilidad+";"+ventas;
//    }



//    @Override
//    public String toString() {
//        return "Tipo de plato: " + tipo +
//                "\n" + nombre + " - Precio: " + precio + "€ - Cantidad disponible: " + disponibilidad;
//    }

}
