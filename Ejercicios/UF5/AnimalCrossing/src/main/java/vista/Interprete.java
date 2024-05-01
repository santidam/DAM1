package vista;

import Entidades.LoQueSea;
import Gestor.Gestor;

import java.util.ArrayList;

public class Interprete {
    private Gestor g = new Gestor();
    private ArrayList<LoQueSea> listaLoQueSeas = g.getListaPlatos();


    public static boolean valName(String name, String tipo) {
        name = name.trim();

        if (name.isEmpty()) {
            System.out.println("Error; no has introducio ningun dato");
            return false;
        }
        String[] partes = name.split("\\s+");

        if (tipo.equals("apellido") && partes.length != 2) {
            System.out.println("Error: debes introducir dos apellidos");
            return false;
        }
        if (tipo.equals("nombre") && partes.length > 2) {
            System.out.println("Error: debes introducir un máximo de dos nombres");
            return false;
        }

        for (String part : partes) {
            if (part.length() < 2 || part.length() > 20) {
                System.out.println("Error: cada parte del " + tipo + " debe tener al menos 2 caracteres y un máximo de 20.");
                return false;
            } else if (!part.matches("[\\p{L}]+")) {
                System.out.println("Error: solo puedes introducir caracteres alfabéticos en cada parte del " + tipo);
                return false;
            }
        }

        return true;
    }
    public boolean valLength(int argsLength,int lengthEsperada) {
        boolean Validacion = false;
        if (argsLength == lengthEsperada) {
            Validacion = true;
        } else {
            System.out.println("ERROR. El número de argumentos es incorrecto.");
        }
        return Validacion;
    }
    public static boolean valDni(String dni) {
        dni = dni.strip().toUpperCase();
        boolean isValid = false;
        int resto = 0;
        String dniNum = getNumDni(dni);
        int numDni = 0;
        String validLetters = "TRWAGMYFPDXBNJZSQVHLCKE";

        if (dniNum.length() == 8 && dni.length() == 9) {
            numDni = toInt(dniNum);
            char letter = dni.charAt(dni.length() - 1);

            resto = numDni % 23;
            if (letter == validLetters.charAt(resto)) {
                isValid = true;

            } else {
                System.out.println("El último carácter del DNI solo puede ser una letra y tiene que ser válida");
            }
        } else {
            System.out.println("El formato del DNi debe ser '12345678X'");
        }

        return isValid;
    }

    public static String getNumDni(String dni) {
        String validNumbers = "0123456789";
        String numDni = "";
        for (int i = 0; i < dni.length() - 1; i++) {
            for (int j = 0; j < validNumbers.length(); j++) {
                if (dni.charAt(i) == validNumbers.charAt(j)) {
                    numDni += dni.charAt(i);
                }
            }
        }
        return numDni;
    }

    public static boolean valInt(String numero, String messageError) {
        try {
            Integer.parseInt(numero);
            return true;
        } catch (NumberFormatException ex) {
            System.out.println(messageError);
            return false;
        }
    }

    public static boolean valDouble(String numero, String message) {
        try {
            Double.parseDouble(numero);
            return true;
        } catch (NumberFormatException ex) {
            System.out.println(message);
            return false;
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

