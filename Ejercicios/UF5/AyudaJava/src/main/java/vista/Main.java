package vista;
import Exceptions.ComandaExeption;

public class Main {
    public static void main(String[] args)  {
        AskData input = new AskData();
        Interprete i = new Interprete();
        boolean salir = false;


        do {
            

                try {

                args = input.askString("> ").split(" ");


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

                                break;
                            case "request": // peticion servicio

                                break;
                            case "finish":// finalizar peticion

                                break;
                            case "leave":// liberar habitacion

                                break;
                            case "money": // Mostrar dinero actual

                                break;
                            case "exit": // Salir
                                if (args.length != 1) {
                                    throw new ComandaExeption(ComandaExeption.ARGS_INCORRECTOS);
                                }
                                salir = true;
                                break;
                            default:
                                throw new ComandaExeption(ComandaExeption.OPERACION_INCORRECTA);

                        }

//                    }
                } catch (ComandaExeption e) {
                    System.out.println(e);
                }




        }while (!salir);



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