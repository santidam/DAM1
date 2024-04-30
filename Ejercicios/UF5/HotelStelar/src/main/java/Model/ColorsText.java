package Model;

public class ColorsText {
    public static final String ANSI_RESET = "\033[0m";
    public static final String ANSI_RED = "\033[31m";
    public static final String ANSI_MAGENTA = "\033[35m";
    public static final String ANSI_BLUE = "\033[34m";

    public static String textAnswer(String s){
        return ANSI_BLUE+ "--> " + s + " <--" + ANSI_RESET;
    }
    public static String textERROR(String s){
        return ANSI_RED+ "[ " + s + " ]" + ANSI_RESET;
    }
    public static String textINFO(String s){
        return ANSI_MAGENTA+ s+ ANSI_RESET;
    }
}
