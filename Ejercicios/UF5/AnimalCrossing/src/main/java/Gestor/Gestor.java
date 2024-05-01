package Gestor;

import Entidades.LoQueSea;

import java.util.ArrayList;

public class Gestor {

    private Persistence filePLatos = new Persistence("dades","persistencia.txt");

    private ArrayList<LoQueSea> listaLoQueSeas;


    public Gestor(){
        listaLoQueSeas = new ArrayList<>();
        cargarFicheros();
    }

    public void cargarFicheros(){
        this.listaLoQueSeas = (ArrayList<LoQueSea>) filePLatos.read();

    }



    public LoQueSea isPlato(String name, ArrayList<LoQueSea> lista){
        if (listaLoQueSeas.isEmpty()){
            return null;
        }else {
            for (LoQueSea p: listaLoQueSeas){
                if (p.getNombre().equals(name)) {
                    return p;
                }
            }
        }
        return null;
    }

    public ArrayList<LoQueSea> getListaPlatos() {
        return listaLoQueSeas;
    }

    //    public ArrayList<Object> toObjectList(String tipo){
//        ArrayList<Object> listaObjetos = new ArrayList<>();
//        switch (tipo){
//            case "plato":
//                for (Plato c: listaPlatos){
//                    listaObjetos.add((Object) c);
//                }
//                break;
//            case "placa":
//                for (Placa p:listaPlacas){
//                    listaObjetos.add((Object) p);
//                }
//                break;
//            case "aparato":
//                for (Aparato a:listaAparatos){
//                    listaObjetos.add((Object) a);
//                }
//                break;
//        }
//        return listaObjetos;
//    }

}
