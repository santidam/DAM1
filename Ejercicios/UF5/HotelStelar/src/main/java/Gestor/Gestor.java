package Gestor;

import Model.*;
import Exceptions.ComandaExeption;

import java.awt.image.ImageProducer;
import java.util.*;

public class Gestor {

    private Persistence filePLatos = new Persistence("dades","persistencia.txt");

    private ArrayList<Habitacion> listaHabitaciones;
    private ArrayList<Persona> listaPersonas;
    private HashSet<String> peticionesPendientes;
    private Hotel hotel;



    public Gestor(){
        listaHabitaciones = new ArrayList<>();
        listaPersonas = new ArrayList<>();
        peticionesPendientes = new HashSet<>();
        hotel = new Hotel();
//        cargarFicheros();
    }

    public void cargarFicheros(){
        this.listaHabitaciones = (ArrayList<Habitacion>) filePLatos.read();

    }
    public String addRoom(String numero ,int capacidad, String[] serveis){
        Habitacion h = new Habitacion(numero,capacidad, serveis );
        listaHabitaciones.add(h);
        hotel.addRoomList(h);
        return ColorsText.textAnswer("New ROOM added "+ numero);
    }
    public String addWorker(String dni, String nombre, String[] habilidades){
        Worker w = new Worker(dni,nombre,habilidades);
        listaPersonas.add(w);
        hotel.addWorkersList(w);
        return ColorsText.textAnswer("New worker added "+dni);

    }
    public String addReservation(String dni, int capacidad, String[] servicios) throws ComandaExeption {
        Habitacion h = valRequeriments(capacidad,servicios);
        if (h==null){
            hotel.restMoney(100);
            throw new ComandaExeption(ComandaExeption.HABITACIONES_NO_CUMPLEN_REQUERIMIENTOS);
        }
        Customer c = new Customer(dni,capacidad,servicios);
        h.setCustomer(c);
        h.setEstado("reserved");
        listaPersonas.add(c);
        return ColorsText.textAnswer("Assigned "+dni+" to Room "+ h.getNumero());
    }
    public Habitacion valRequeriments(int capacidad, String[] servicios){
        ArrayList<Habitacion> lista = new ArrayList<>();
        HashSet<String> setServicios = new HashSet<>(Arrays.asList(servicios));
        Habitacion ha = null;
        for (Habitacion h: listaHabitaciones){
            if (h.getEstado().equals("clean") && h.getCapacidad()>= capacidad && h.getServicios().containsAll(setServicios)){
                lista.add(h);
                if (ha==null || ha.getCapacidad()<h.getCapacidad()){
                    ha = h;
                }
            }
        }
        if (lista.isEmpty()){
            return null;
        }
        Collections.sort(lista);
        return lista.get(0);
    }
    public String listHotel(){
        String s = "==> ROOMS <==";
        if (listaHabitaciones.isEmpty()){
            s+="\n== There is not ROOMS in the Hotel ==";
        }else{
            Collections.sort(listaHabitaciones, new Comparator<Habitacion>() {
                @Override
                public int compare(Habitacion o1, Habitacion o2) {
                    return Integer.parseInt(o1.getNumero())-Integer.parseInt(o2.getNumero());
                }
            });
            for (Habitacion h: listaHabitaciones){
                if (h.getCustomer()==null){
                    s+="\n== ROOM "+h.getNumero()+" "+h.getEstado().toUpperCase()+" ==";
                }else{
                    Customer c = h.getCustomer();
                    s+="\n== ROOM "+h.getNumero()+" CUSTOMER:"+c.getDNI()+"("+c.getCantidadPersonas()+") ==";
                }
            }
        }
        s+="\n====================================================================================================";
        s+="\n==> WORKERS <==";
        int contador = 0;
        for (Persona p:listaPersonas){
            if (p instanceof Worker){
                Worker w = (Worker) p;
                contador++;
                if (w.getEstado().equals("available")){
                    s+="\n== WORKER "+w.getDNI()+ " " +w.getNombre()+" "+w.getEstado().toUpperCase();
                }else{
                    s+="\n== WORKER "+w.getDNI()+ " " +w.getNombre()+" ROOM:"+w.getEstado()+" ==";
                }
            }
        }
        if (contador==0){
            s+="\n== There is not WORKERS in the Hotel";
        }
        s+="\n====================================================================================================";
        return ColorsText.textINFO(s);
    }
    public String problem(Habitacion h) throws ComandaExeption{
        Customer c = h.getCustomer();
        h.setEstado("broken");
        h.setCustomer(null);
        String s = "Room set as BROKEN";
        if (c!=null){
            String dni =  c.getDNI();
            int capacidad = c.getCantidadPersonas();
            String[] requisitos = c.getRequisitosHabitacion();
            listaPersonas.remove(c);
            System.out.println(ColorsText.textAnswer(s));
            return addReservation(dni,capacidad,requisitos);
        }
        return ColorsText.textAnswer(s);

    }
    public void addRequest(Habitacion h, String[] serveis){
        String s = "";
        if (h.getCustomer()==null){
            h.setEstado("broken");
        }
        for (String a: serveis){
            Worker w = valRequest(a);
            if (h.getPeticiones().containsKey(a)){
                System.out.println(ColorsText.textERROR("[ La peticion introducida: "+ a.toUpperCase()+ " ya se encontraba registrada"));
            }else if (w==null){
                h.addPeticion(a,w);
                peticionesPendientes.add(h.getNumero()+":"+a);
                System.out.println(ColorsText.textAnswer("No worker available for this service. Added to customer pending request"));
//                s += "--> No worker available for this service. Added to customer pending request <--\n";
            }else{
                w.setEstado(h.getNumero());
                h.addPeticion(a,w);
                System.out.println(ColorsText.textAnswer("Worker "+ w.getNombre() +" assigned to Room " + h.getNumero()));
                if (h.getCustomer()==null){

                }
//                s+= "--> Worker "+ w.getNombre() + " assigned to Room "+ h.getNumero()+" <--\n";

            }
        }
        HashMap<String,Worker> prueba = h.getPeticiones();
        for (String k: prueba.keySet()){
            Worker w = prueba.get(k);
            if (w==null){
                System.out.println("CLAVE: "+k+" WORKER: "+ w);
            }else{
                System.out.println("CLAVE: "+k+" WORKER: "+ w.getNombre());
            }
        }

//        return ColorsText.textAnswer(s);

    }
    public Worker valRequest(String s){
        for (Persona p: listaPersonas){
            if (p instanceof Worker){
                Worker w = (Worker) p;
                if (w.getHabilidad().contains(s) && w.getEstado().equals("available")){
                    return w;
                }
            }
        }
        return null;
    }
    public void finish(Habitacion h){
        HashMap<String,Worker> peticiones = h.getPeticiones();
        ArrayList<String> clavesEliminar = new ArrayList<>();
        int contador = 0;
        for (String clave:peticiones.keySet()){
            Worker w = peticiones.get(clave);
            if (w!=null){
                contador++;
                w.setEstado("available");
                clavesEliminar.add(clave);
            }
        }if (contador==0){
            System.out.println(ColorsText.textAnswer(" There aren't workers in room"));
        }else{
            for (String s: clavesEliminar){
                h.removePeticion(s);
            }
            System.out.println(ColorsText.textAnswer("Services finished in room: " +h.getNumero()));
            reasignarWorker();
            if (h.getPeticiones().isEmpty() && h.getCustomer()!=null){
                h.setEstado("reserved");
            } else if (h.getPeticiones().isEmpty() && h.getCustomer() == null) {
                h.setEstado("clean");
            }
        }

    }
    public void reasignarWorker(){
        ArrayList<String> listaReubicaciones = new ArrayList<>();
        if (!peticionesPendientes.isEmpty()){
            for (String s: peticionesPendientes){
                String[] args = s.split(":");
                Worker w = valRequest(args[1]);
                if (w!=null){
                    Habitacion h = isLista(args[0],listaHabitaciones);
                    h.addPeticion(args[1],w);
                    w.setEstado(h.getNumero());
                    System.out.println("Trabajador "+ w.getNombre()+ " reubicado en ROOM :" + h.getNumero());
                    listaReubicaciones.add(s);
                }
            }
            for (String s: listaReubicaciones){
                peticionesPendientes.remove(s);
            }
        }
    }
    public void leave(Habitacion h, int money){
        // ARREGLAR SALIDA de EMPLEADOS -> mirar lista
        ArrayList<String> listaTareasRemove = new ArrayList<>();
        String string ="Room "+h.getNumero()+" free and set to UNCLEAN";
        h.setEstado("unclean");
        h.setCustomer(null);
        System.out.println(ColorsText.textAnswer(string));

        for (String s: peticionesPendientes){
            if (s.contains(h.getNumero())){
                listaTareasRemove.add(s);
            }
        }
        if (listaTareasRemove.isEmpty()){
            h.clearPeticiones();
            liberarWorker(h);
            hotel.sumMoney(money);
            System.out.println(ColorsText.textAnswer("Satisfied clients. You win "+money+" €"));
        }else{
            for (String s:listaTareasRemove){
                peticionesPendientes.remove(s);
            }
            liberarWorker(h);
            h.clearPeticiones();
            double finalMoney = (double) money /2;
            hotel.restMoney(finalMoney);
            reasignarWorker();
            System.out.println(ColorsText.textAnswer("Unsatisfied clients. You loose "+finalMoney+" €"));

        }
//        if (h.getPeticiones().isEmpty()){
//            hotel.sumMoney(money);
//            System.out.println(ColorsText.textAnswer("Satisfied clients. You win "+money+" €"));
//        }else{
//            ArrayList<String> listaTareasRemove = new ArrayList<>();
//            for (Persona p: listaPersonas){
//                if (p instanceof Worker){
//                    Worker w = (Worker) p;
//                    if (w.getEstado().contains(h.getNumero())){
//                        w.setEstado("available");
//                    }
//                }
//            }
//            for (String s: peticionesPendientes){
//                if (s.contains(h.getNumero())){
//                    listaTareasRemove.add(s);
//                }
//            }
//            for (String s: listaTareasRemove){
//                peticionesPendientes.remove(s);
//            }
//            h.clearPeticiones();
//            double finalMoney = (double) money /2;
//            hotel.restMoney(finalMoney);
//            System.out.println(ColorsText.textAnswer("Unsatisfied clients. You loose "+finalMoney+" €"));
//
//        }

    }
    public String showMoney(){
        return ColorsText.textINFO("==========================================================================================================="+
                "\n==>     MONEY  :  "+ hotel.getDinero()+"  €     <=="+
                "\n===========================================================================================================");
    }
    public void liberarWorker(Habitacion h){
        for (Persona p: listaPersonas){
            if (p instanceof Worker) {
                Worker w = (Worker) p;
                if (w.getEstado().contains(h.getNumero())) {
                    w.setEstado("available");
                }
            }
        }
        reasignarWorker();
    }
    public Habitacion isLista(String numero, ArrayList<Habitacion> lista){
        if (lista.isEmpty()){
            return null;
        }else {
            for (Habitacion p: lista){
                if (p.getNumero().equals(numero)) {
                    return p;
                }
            }
        }
        return null;
    }
    public Persona isListaPersona(String dni, ArrayList<Persona> lista,String tipo){
        if (lista.isEmpty()){
            return null;
        }else {
            for (Persona p: lista){
                if (tipo.equals("worker") && p instanceof Worker && p.getDNI().equals(dni)){
                    return p;
                } else if (tipo.equals("customer") && p instanceof Customer && p.getDNI().equals(dni)) {
                    return p;
                }
            }
        }
        return null;
    }

    public ArrayList<Habitacion> getListaHabitaciones() {
        return listaHabitaciones;
    }

    public ArrayList<Persona> getListaPersonas() {
        return listaPersonas;
    }
}
