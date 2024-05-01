package vista;

import Enum.*;
import Exceptions.ComandaExeption;

import Model.Customer;
import Model.Habitacion;
import Model.Persona;
import Model.Worker;

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;

public class Interprete {

    private int dinero = 1000;
    private HashMap<String, Habitacion> listaHabitaciones = new HashMap<>();
    private HashMap<String, Persona> listaPersonas = new HashMap<>();




    public void valRoom(String[] args) throws ComandaExeption{
        valLength(args.length, 4);  // logitud args
        String room = args[1]; //separando entradas args
        int capacidad = valIntMin(args[2],1 );
        valNumRoom(args[1]); // valorando args
        Habitacion h = listaHabitaciones.get(args[1]); //habitacion existe ?
        if (h!=null){
            throw new ComandaExeption(ComandaExeption.HABITACION_EXISTENTE);
        }
        String[] serveis = args[3].split(","); // separamos por "," en una lista para servicios
        valServei(serveis); // Comprobamos con enums
        room(room,capacidad,serveis); // llamamos al metodo final



    }

    public void room (String room, int capacidad, String[] serveis){
        Habitacion h = new Habitacion(room,capacidad, toHashSet(serveis) ); // creamos haitacion
        listaHabitaciones.put(room, h); // añadir a la lista de habitaciones
        System.out.println("Habitacion registrada");
    }


    public void valWorker(String[] args) throws ComandaExeption{
        valLength(args.length, 4);
        valDNI(args[1]);
        String[] habilidades = args[3].split(",");
        valHabilidades(habilidades);
        Persona p = listaPersonas.get(args[1]);
        if (p!=null){
            throw new ComandaExeption(ComandaExeption.WORKER_EXISTENTE);
        }
        worker(args[1],args[2],habilidades );

    }

    public void worker(String dni, String nombre, String[] habilidades){
        Worker w = new Worker(dni,nombre,toHashSet(habilidades));
        listaPersonas.put(dni, w);
        System.out.println("Trabajador registrado");
    }

    public void valReservation(String[] args) throws ComandaExeption {
        valLength(args.length, 4);
        valDNI(args[1]);
        Persona p = listaPersonas.get(args[1]);
        if (p!=null){
            throw new ComandaExeption(ComandaExeption.YA_EXISTE);
        }
        int capacidad =  valIntMin(args[2], 1);
        String[] serveis = args[3].split(",");
        valServei(serveis);
        reservation(args[1],capacidad, serveis );
    }
    public void reservation(String dni, int capacidad, String[] serveis) throws ComandaExeption {
        HashSet<String> serv = toHashSet(serveis);
        Habitacion h = valRequisitos(capacidad, serv);
        if (h==null){
            throw new ComandaExeption(ComandaExeption.HABITACIONES_NO_CUMPLEN_REQUERIMIENTOS);
        }
        Customer c = new Customer(dni, capacidad, serv);
        h.setEstado("reserved");
        h.setCustomer(c);
        listaPersonas.put(dni,c);
        System.out.println("Habitacion asignada " + dni + " Room "+ h.getNumero());

    }
    public Habitacion valRequisitos(int capacidad, HashSet<String> serveis){
        Habitacion ha = null;
        for (Habitacion h: listaHabitaciones.values()){
            if (h.getEstado().equals("clean") && h.getCapacidad()>=capacidad && h.getServeis().containsAll(serveis)){
                if (ha == null || ha.getCapacidad()>h.getCapacidad()){
                    ha = h;
                }
            }
        }
        return ha;
    }

    public void valHotel(String[] args) throws ComandaExeption{
        valLength(args.length,1 );
        hotel();
    }


    public void hotel(){
        System.out.println("==> ROOMS <==");
        if (listaHabitaciones.isEmpty()){
            System.out.println("No hay habitaciones registradas");
        }else{
            for (Habitacion h: listaHabitaciones.values()){
                System.out.println("== "+h+" ==");
            }
        }
        System.out.println("=============================================================");
        System.out.println("==> WORKERS <==");
        int contador = 0;
        for (Persona p: listaPersonas.values()){
            if (p instanceof Worker w){
                System.out.println("== "+w+" ==");
                contador++;
            }
        }
        if (contador == 0){
            System.out.println("No hay trabajdores registrados");
        }

    }
    public double media(int[] listaNumeros) throws ComandaExeption {
        if (listaNumeros.length==0){
            throw new ComandaExeption(ComandaExeption.NO_SE_PUEDE_DIVIDIR_CERO);
        }
        double n = 0;
        for (int numero: listaNumeros){
            n+= numero;
        }
        return n/listaNumeros.length;

    }


    public void valDNI(String s) throws ComandaExeption{
        if (s.length()!=8){
            throw new ComandaExeption(ComandaExeption.DATO_INCORRECTO);
        }
        valInt(s);
    }




    public void valNumRoom(String numero)throws ComandaExeption{
        if (numero.length()!=3){
            throw new ComandaExeption(ComandaExeption.DATO_INCORRECTO);
        }
        valInt(numero);
    }

    public HashSet<String> toHashSet (String[] args){
        HashSet<String> s = new HashSet<>(Arrays.asList(args));
        return s;
    }




    public void valEstadoHabitacion(String[] args) throws ComandaExeption{
        try{
            for (String s: args){
                EstadoHabitacion.valueOf(s);
            }

        }catch (IllegalArgumentException e){
            throw new ComandaExeption(ComandaExeption.ESTADO_HABITACION_INCORRECTO);
        }
    }

    public void valHabilidades(String[] args) throws ComandaExeption{
        try{
            for (String s: args){
                Habilidades.valueOf(s);
            }

        }catch (IllegalArgumentException e){
            throw new ComandaExeption(ComandaExeption.HABILIDAD_INCORRECTA);
        }
    }

    public void valServei(String[] args) throws ComandaExeption{
        try{
            for (String s: args){
                Serveis.valueOf(s);
            }

        }catch (IllegalArgumentException e){
            throw new ComandaExeption(ComandaExeption.SERVICIO_INCORRECTO);
        }
    }

    public void valLength(int argsLength,int lengthEsperada) throws ComandaExeption {
        if (argsLength!=lengthEsperada){
            throw new ComandaExeption(ComandaExeption.ARGS_INCORRECTOS);
        }
    }

    public int valIntMin(String numero, int min) throws ComandaExeption{
        valInt(numero);
        if (Integer.parseInt(numero)<min){
            throw new ComandaExeption(ComandaExeption.NUMERO_MENOR_UNO);
        }
        return Integer.parseInt(numero);
    }
    public void valInt(String numero) throws ComandaExeption{
        try {
            Integer.parseInt(numero);

        } catch (NumberFormatException ex) {
            throw new ComandaExeption(ComandaExeption.TIPO_ENTERO_INCORRECTO);
        }
    }

    public static void valDouble(String numero, String message) throws ComandaExeption{
        try {
            Double.parseDouble(numero);
        } catch (NumberFormatException ex) {
            System.out.println(message);
            throw new ComandaExeption(ComandaExeption.DATO_INCORRECTO);
        }
    }

    public static int toInt(String num) {
        //habrá que poner una excepcioón para asegurar que sea un int
        return Integer.parseInt(num);
    }

    public static double toDouble(String num) {
        //habrá que poner una excepcioón para asegurar que sea un double
        return Double.parseDouble(num);
    }


}

