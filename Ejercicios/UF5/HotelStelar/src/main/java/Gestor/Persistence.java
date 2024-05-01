package Gestor;


import Model.Habitacion;

import java.io.*;
import java.util.ArrayList;

public class Persistence {

    private String fileName;
    private String pathFile;
    private File folderFile;

    public Persistence(String folder, String file) {
        folder = "." +File.separator+folder;
        fileName = file;
        pathFile = folder + File.separator + fileName;
        folderFile = new File(folder);
    }

    public void write(Habitacion p) {
        if (!folderFile.exists()) {
            folderFile.mkdir();
        }
        try {
            BufferedWriter bw = new BufferedWriter(new FileWriter(pathFile, true));
//            bw.write(p.toStringWrite());
            bw.newLine();
            bw.close();
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }
    }

    public void sobreEscribir(ArrayList<Habitacion> lista) {

        if (!this.folderFile.exists()) {
            this.folderFile.mkdir();
        }
        try {
            BufferedWriter bw = new BufferedWriter(new FileWriter(pathFile, false));
            for (Habitacion p: lista){
//                bw.write(p.toStringWrite());
                bw.newLine();
            }

            bw.close();
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }
    }

    public Object read() {
        ArrayList<Object> listaObjetos = new ArrayList<>();
        if (!folderFile.exists()) {
            return listaObjetos;
        } else {
            File f = new File(pathFile);
            if (!f.exists()) {
                return listaObjetos;
            } else {
                try {
                    BufferedReader br = new BufferedReader(new FileReader(f));
                    String linea;
                    while ((linea = br.readLine()) != null) {
                        String[] parameters = linea.split(";");
//                        Habitacion p = new Habitacion(parameters[0],parameters[1], Double.parseDouble(parameters[2]));
//                        listaObjetos.add(p);
//                        p.setDisponibilidad(Integer.parseInt(parameters[3]));
//                        p.setVentas(Integer.parseInt(parameters[4]));
                        }


                    br.close();
                } catch (IOException ex) {
                    System.out.println(ex.getMessage());
                }
            }
        }

        return listaObjetos;
    }

}
