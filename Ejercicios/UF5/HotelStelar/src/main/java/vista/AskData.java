package vista;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class AskData {

    private BufferedReader br;

    public AskData() {
        br = new BufferedReader(new InputStreamReader(System.in));
    }
    public String askString(String message){
        System.out.print(message);
        String word = "";
        try {
            do {
                word = br.readLine().toLowerCase().trim();
                if (word.isEmpty()){
                    System.out.println("ERROR. Debes introducir al menos un caracter");
                    System.out.print("> ");
                }
            }while (word.isEmpty());

        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return word;
    }
    public double askDouble(String message){
        System.out.println(message);
        double num = 0;
        boolean error = true;
        while (error) {
            try {
                num = Double.parseDouble(br.readLine());
                error = false;
            } catch (IOException ex) {
                System.out.println(ex.getMessage());
            } catch (NumberFormatException ex) {
                System.out.println("Debes introducir un número valido");
            }
        }
        return num;

    }
    public double askDouble(String message, String messageError, int min){
        double number = 0;
        do {
            number = askDouble(message);
            if (number < min) {
                System.out.println(messageError);
            }
        } while (number < min);
        return number;
    }
    public double askDouble(String message, String messageErrorMin, String messageErrorMax,int min, int max) {
        double number = 0;
        do {
            number = askDouble(message);
            if (number < min) {
                System.out.println(messageErrorMin);
            } else if (number > max) {
                System.out.println(messageErrorMax);
            }
        } while (number < min || number > max);
        return number;
    }
    public int askInt(String message) {
        System.out.println(message);
        int number = 0;
        boolean error = true;
        while (error) {
            try {
                number = Integer.parseInt(br.readLine());
                error = false;
            } catch (IOException ex) {
                System.out.println(ex.getMessage());
            } catch (NumberFormatException ex) {
                System.out.println("Debes introducir un número entero");
            }
        }
        return number;
    }
    public int askIntMax(String message, String messageError, int max){
        int number = 0;
        do {
            number = askInt(message);
            if (number > max) {
                System.out.println(messageError);
            }
        } while (number > max);
        return number;
    }
    public int askInt(String message, String messageErrorMin, int min) {
        int number = 0;
        do {
            number = askInt(message);
            if (number < min) {
                System.out.println(messageErrorMin);
            }
        } while (number < min );
        return number;
    }
    public int askInt(String message, String messageErrorMin,String messageErrorMax, int min, int max) {
        int number = 0;
        do {
            number = askInt(message);
            if (number < min) {
                System.out.println(messageErrorMin);
            } else if (number > max) {
                System.out.println(messageErrorMax);
            }
        } while (number < min || number > max);
        return number;
    }
}


