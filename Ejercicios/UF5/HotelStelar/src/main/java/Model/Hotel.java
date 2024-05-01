package Model;

import java.util.ArrayList;

public class Hotel {
    private double dinero;
    private ArrayList<Habitacion> habitaciones;
    private ArrayList<Worker> trabajadores;

    public Hotel() {
        this.dinero = 1000;
        this.habitaciones = new ArrayList<>();
        this.trabajadores = new ArrayList<>();
    }

    public double getDinero() {
        return dinero;
    }

    public void sumMoney(double n){
        dinero += n;
    }
    public void restMoney(double n){
        dinero -= n;
    }
    public void addRoomList(Habitacion h){
        habitaciones.add(h);
    }
    public void addWorkersList(Worker w){
        trabajadores.add(w);
    }
}
