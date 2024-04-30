package vista;
import Exceptions.ComandaExeption;

public class Main {
    public static void main(String[] args)  {
        AskData input = new AskData();
        Interprete i = new Interprete();
        boolean salir = false;
        String[] comandosIniciales = prueba();
        int indiceComando = 0;

        do {
            if (indiceComando < comandosIniciales.length) {
                // Procesa cada comando predefinido
                System.out.println(comandosIniciales[indiceComando]);
                args = comandosIniciales[indiceComando++].toLowerCase().split(" ");

            } else {
                // Permite al usuario ingresar comandos después de los predefinidos
                args = input.askString("> ").toLowerCase().split(" ");
            }

                try {

//                args = input.askString("> ").split(" ");
                    if (args.length > 0) {

                        switch (args[0]) {
                            case "room":// Registrar habitacion
                                i.valRoom(args);
                                break;
                            case "worker":// Registrar trabajador
                                i.valWorker(args);
                                break;
                            case "reservation":// regtistrar reserva
                                i.valReservation(args);
                                break;
                            case "hotel": // Info habitaciones
                                i.valHotel(args);
                                break;
                            case "problem"://  registrar problema
                                i.valProblem(args);
                                break;
                            case "request": // peticion servicio
                                i.valRequest(args);
                                break;
                            case "finish":// finalizar peticion
                                i.valFinish(args);
                                break;
                            case "leave":// liberar habitacion
                                i.valLeave(args);
                                break;
                            case "money": // Mostrar dinero actual
                                i.valMoney(args);
                                break;
                            case "exit": // Salir
                                if (args.length != 1) {
                                    throw new ComandaExeption(ComandaExeption.ARGS_INCORRECTOS);
                                }
                                salir = true;
                                break;
                            default:
                                System.out.println("ERROR. debes introducir un comando valido");
                                throw new ComandaExeption(ComandaExeption.OPERACION_INCORRECTA);

                        }

                    }
                } catch (ComandaExeption e) {
                    System.out.println(e);
                }




        }while (!salir);



    }
    public static String[] prueba (){
        return new String[]{
                "ROOM 001 3 tv,jacuzzi,balco",
                "ROOM 002 2 tv,llitdoble",
                "ROOM 003 1 telefon,satelit,tv",
                "ROOM 004 2 suite,jacuzzi,tv,balco,llitdoble,minibar,telefon,satelit",
                "ROOM 005 4 tv,telefon,llitdoble",
                "ROOM 006 1 tv",
                "WORKER 12345678 Pepe piscina,manteniment",
                "WORKER 88888888 Maria manteniment,spa",
                "WORKER 11111111 Juan neteja,bar,menjar,bugaderia",
                "WORKER 22222222 Clara menjar,bar",
                "ROOM 007 LLITDOBLE,TV",
                "ROOM 007 2 LLITDOBLE,TV",
                "room 008 1 satelit,telefon,tv",
                "room 001 1 tv",
                "room 009 2 sauna,satelit,tv",
                "WORKER 33333333 Antonio neteja,manteniment",
                "worker 44444444 Susana piscina,manteniment",
                "worker 33333333 Pepe piscina,manteniment",
                "worker 55555555 Sandra piscina,manteniment,sauna",
                "reservation 11223344 1 tv",
                "reservation 33445566 2 llitdoble,tv,telefon",
                "reservation 55667788 1 TV",
                "RESERVATION 88888888 4 JACUZZI,TV,BALCO",
                "PROBLEM 001",
                "problem 888",
                "problem 004",
                "problem 005",
                "request 001 manteniment,neteja",
                "request 003 piscina,manteniment,neteja",
                "request 006 menjar,bar",
                "request 888 bar",
                "request 001 informatica,neteja",
//                "finish 001",
//                "finish 004",
//                "FINISH 003",
//                "FINISH",
//                "finish 888",
//                "LEAVE 888",
//                "leave 888 500",
//                "leave 600 400",
//                "leave 006 400",
//                "leave 002 250",
//                "money",
//                "hotel"
        };

    }
    public static void menuPrincipal(){
        System.out.println("***** Menu *****" +
                "\nR. Registrar Jugador " +
                "\n2. Cocinar plato" +
                "\n3. Vender plato" +
                "\n4. Plato favorito" +
                "\n5. Mostrar carta" +
                "\n6. Estadisticas" +
                "\n7. Salir");

    }

}