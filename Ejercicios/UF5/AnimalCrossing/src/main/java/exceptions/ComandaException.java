package exceptions;

import java.util.Arrays;
import java.util.List;

/**
 *
 * @author mfontana
 */
public class ComandaException extends Exception {

    public static final int ADD_CASA_ARGS = 0;
    public static final int SUPERFICIE_INT = 1;
    public static final int ADD_PLACA_ARGS = 2;
    public static final int PREU_DOUBLE = 3;
    public static final int POTENCIA_INT = 4;
    public static final int ADD_APARELL_ARGS = 5;
    public static final int ON_CASA_ARGS = 6;
    public static final int ON_APARELL_ARGS = 7;
    public static final int OFF_APARELL_ARGS = 8;
    public static final int LIST_ARGS = 9;
    public static final int INFO_ARGS = 10;
    public static final int QUIT_ARGS = 11;

    private final List<String> missatges = Arrays.asList(
            "ERROR: Número de paràmetres incorrecte.\nÚs: addCasa [nif] [nom] [superficie]",
            "ERROR: Argument incorrecte, la superfície ha de ser un número sencer.",
            "ERROR: Número de paràmetres incorrecte.\nÚs: addPlaca [nif] [superficie] [preu] [potència]",
            "ERROR: Argument incorrecte, el preu ha de ser un número.",
            "ERROR: Argument incorrecte, la potència ha de ser un número sencer.",
            "ERROR: Número de paràmetres incorrecte.\nÚs: addAparell [nif] [descripció] [potència]",
            "ERROR: Número de paràmetres incorrecte.\nÚs: onCasa [nif]",
            "ERROR: Número de paràmetres incorrecte.\nÚs: onAparell [nif] [descripció aparell]",
            "ERROR: Número de paràmetres incorrecte.\nÚs: offAparell [nif] [descripció aparell]",
            "ERROR: Número de paràmetres incorrecte.\nÚs: list",
            "ERROR: Número de paràmetres incorrecte.\nÚs: info [nif]",
            "ERROR: Número de paràmetres incorrecte.\nÚs: quit");

    private final int code;

    public ComandaException(int code) {
        this.code = code;
    }

    @Override
    public String getMessage() {
        return missatges.get(code);
    }
}
