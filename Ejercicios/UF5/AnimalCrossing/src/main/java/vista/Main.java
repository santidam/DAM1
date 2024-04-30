package vista;
import Gestor.Gestor;
import Entidades.*;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Gestor g = new Gestor();
        AskData input = new AskData();
        Interprete i = new Interprete();
        boolean salir = false;
        while (!salir){
            menuPrincipal();
            String entrada = input.askString("Indica una opción: ");
            if (entrada.equals("7")){
                System.out.println("Cerrando programa...");
                salir = true;
            }else{
                String nombre;
                String tipo;
                switch (entrada){
                    case "1"://
                        break;
                    case "2"://
                        break;
                    case "3"://
                        break;
                    case "4"://
                        break;
                    case "5": //
                        break;
                    case "6"://
                        break;
                    default:
                        System.out.println("ERROR. debes introducir un comando valido");
                        break;
                }

            }
        }

    }
    public static void menuPrincipal(){
        System.out.println("***** Tapera Thor Tilla *****" +
                "\n1. Registrar plato " +
                "\n2. Cocinar plato" +
                "\n3. Vender plato" +
                "\n4. Plato favorito" +
                "\n5. Mostrar carta" +
                "\n6. Estadisticas" +
                "\n7. Salir");

    }

}