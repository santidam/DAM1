package vista;

import Model.Customer;
import Model.Habitacion;
import Model.Persona;
import Model.Worker;
import Exceptions.ComandaExeption;
import Gestor.Gestor;
import Enum.*;

import java.util.ArrayList;

public class Interprete {
    private Gestor g = new Gestor();
    private ArrayList<Habitacion> listasHabitaciones = g.getListaHabitaciones();
    private ArrayList<Persona> listaPersona = g.getListaPersonas();
    public void valRoom(String[] args) throws ComandaExeption{
        valLength(args.length, 4);
        if (args[1].length()!=3){
            throw new ComandaExeption(ComandaExeption.DATO_INCORRECTO);
        }
        valInt(args[1]);
        valIntMin(args[2],1);
        int capacidad = Integer.parseInt(args[2]);
        Habitacion room = g.isLista(args[1],listasHabitaciones );
        if (room!=null){
            throw new ComandaExeption(ComandaExeption.HABITACION_EXISTENTE);
        }
        String[] servicios = args[3].split(",");
        valServei(servicios);
        System.out.println(g.addRoom(args[1],capacidad, servicios));

    }
    public void valWorker(String[] args) throws ComandaExeption{
        valLength(args.length, 4);
        valDNI(args[1]);
        String[] habilidades = args[3].split(",");
        valHabilidad(habilidades);
        Worker w = (Worker) g.isListaPersona(args[1],listaPersona, "worker" );
        if (w!=null){
            throw new ComandaExeption(ComandaExeption.WORKER_EXISTENTE);
        }
        System.out.println(g.addWorker(args[1],args[2],habilidades));

    }
    public void valReservation(String[] args) throws ComandaExeption{
        valLength(args.length,4);
        valDNI(args[1]);
        valIntMin(args[2],1);
        int capacidad = Integer.parseInt(args[2]);
        String[] servicios = args[3].split(",");
        Customer c = (Customer) g.isListaPersona(args[1], listaPersona, "customer");
        if (c!=null){
            throw new ComandaExeption(ComandaExeption.CLIENTE_EXISTENTE);
        }
        valServei(servicios);
        System.out.println(g.addReservation(args[1], capacidad, servicios));
    }
    public void valHotel(String[] args) throws ComandaExeption{
        valLength(args.length,1);
        System.out.println(g.listHotel());
    }
    public void valProblem(String[] args) throws ComandaExeption{
        valLength(args.length,2);
        valInt(args[1]);
        Habitacion h = g.isLista(args[1], listasHabitaciones );
        if (h==null){
            throw new ComandaExeption(ComandaExeption.HABITACION_NO_EXISTE);
        }
        System.out.println(g.problem(h));
    }
    public void valRequest(String[] args) throws ComandaExeption{
        valLength(args.length,3);
        if (args[1].length()!=3){
            throw new ComandaExeption(ComandaExeption.DATO_INCORRECTO);
        }
        valInt(args[1]);
        String[] serveis = args[2].split(",");
        valHabilidad(serveis);
        Habitacion h = g.isLista(args[1], listasHabitaciones);
        if (h==null){
            throw new ComandaExeption(ComandaExeption.HABITACION_NO_EXISTE);
        }
        g.addRequest(h,serveis);

    }
    public void valFinish(String[] args) throws ComandaExeption{
        valLength(args.length,2);
        valRoomNumber(args[1]);
        Habitacion h = g.isLista(args[1], listasHabitaciones );
        if (h==null){
            throw new ComandaExeption(ComandaExeption.HABITACION_NO_EXISTE);
        }
        g.finish(h);
    }
    public void valLeave(String[] args) throws ComandaExeption{
        valLength(args.length, 3);
        valRoomNumber(args[1]);
        Habitacion h = g.isLista(args[1],listasHabitaciones );
        if (h==null){
            throw new ComandaExeption(ComandaExeption.HABITACION_NO_EXISTE);
        }
        if (h.getCustomer()==null){
            throw new ComandaExeption(ComandaExeption.HABITACION_SIN_CLIENTE);
        }
        valIntMin(args[2],1 );
        int money = Integer.parseInt(args[2]);
        g.leave(h, money);

    }
    public void valMoney(String[] args) throws ComandaExeption{
        valLength(args.length, 1);
        System.out.println(g.showMoney());
    }
    public void valRoomNumber(String s) throws ComandaExeption{
        if (s.length()!=3){
            throw new ComandaExeption(ComandaExeption.DATO_INCORRECTO);
        }
        valInt(s);
    }
    public void valDNI(String s) throws ComandaExeption{
        valInt(s);
        if (s.length()!=8){
            throw new ComandaExeption(ComandaExeption.DNI_NO_VALIDO);
        }
    }
    public void valHabilidad(String[] args )throws ComandaExeption{
        try{
            for (String s: args){
                Habilidades.valueOf(s);
            }

        }catch (IllegalArgumentException e){
            throw new ComandaExeption(ComandaExeption.SERVICIO_INCORRECTO);
        }
    }
    public void valServei(String[] args) throws ComandaExeption{
        try{
            for (String s: args){
                Servicios.valueOf(s);
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

    public void valIntMin(String numero, int min) throws ComandaExeption{
        valInt(numero);
        if (Integer.parseInt(numero)<min){
            throw new ComandaExeption(ComandaExeption.NUMERO_MENOR_UNO);
        }
    }
    public static void valInt(String numero) throws ComandaExeption{
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

