
package exceptions;

import java.util.Arrays;
import java.util.List;

/**
 *
 * @author mfontana
 */
public class EndollsException extends Exception {
    
    public static final int SUPERFICIE_CASA_ERROR = 0;
    public static final int CASA_EXISTENT = 1;
    public static final int CASA_NO_EXISTEIX = 2;
    public static final int SUPERFICIE_PLACA_ERROR = 3;
    public static final int PREU_ERROR = 4;
    public static final int POTENCIA_ERROR = 5;
    public static final int PLACA_NO_CAP = 6;
    public static final int APARELL_EXISTENT = 7;
    public static final int CASA_ENCESA = 8;
    public static final int APARELL_NO_EXISTEIX = 9;
    public static final int APARELL_ENCES = 10;
    public static final int CASA_APAGADA = 11;
    public static final int PLOMS = 12;
    public static final int APARELL_APAGAT = 13;
    
    private final List<String> missatges = Arrays.asList(
            "ERROR: Superficie incorrecta. Ha de ser més gran de 10.",
            "ERROR: Ja hi ha una casa registrada amb aquest nif",
            "ERROR: No hi ha cap casa registrada amb aquest nif.",
            "ERROR: Superfície incorrecta. Ha de ser més gran de 0.",
            "ERROR: Preu incorrecte. Ha de ser més gran de 0.",
            "ERROR: Potència incorrecte. Ha de ser més gran de 0.",
            "ERROR: No hi ha espai disponible per a instal·lar aquesta placa.",
            "ERROR: Ja existeix un aparell amb aquesta descripció a la casa indicada.",
            "ERROR: La casa ja té l'interruptor encès.",
            "ERROR: No hi ha cap aparell registrat amb aquesta descripció a la casa indicada.",
            "ERROR: L'aparell ja està encès.",
            "ERROR: No es pot encendre l'aparell. L'interruptor general està apagat.",
            "ERROR: Han saltat els ploms. La casa ha quedat completament apagada.",
            "ERROR: L'aparell ja està apagat.");
    
    private final int code;

    public EndollsException(int code) {
        this.code = code;
    }


    @Override
    public String getMessage() {
        return missatges.get(code);
    }
}
