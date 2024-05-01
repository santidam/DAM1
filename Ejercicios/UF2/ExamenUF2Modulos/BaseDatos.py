# En este módulo se almacenarán las bases de datos del programa, siendo accesibles
# desde el módulo interpret

from datetime import datetime, date, timedelta

diccMision = {}
diccMision = {}

diccMision["mision1"] = {"lugar": "Ciudad A", "fecha": "05-02-2024"}
diccMision["mision2"] = {"lugar": "Ciudad B", "fecha": "04-02-2024"}
diccMision["mision3"] = {"lugar": "Ciudad C", "fecha": "15-02-2024"}
diccMision["mision4"] = {"lugar": "Ciudad D", "fecha": "20-02-2024"}
diccMision["mision5"] = {"lugar": "Ciudad E", "fecha": "25-02-2024"}
diccMision["mision6"] = {"lugar": "Ciudad F", "fecha": "02-03-2024"}
diccMision["mision7"] = {"lugar": "Ciudad G", "fecha": "07-03-2024"}
diccMision["mision8"] = {"lugar": "Ciudad H", "fecha": "12-03-2024"}
diccMision["mision9"] = {"lugar": "Ciudad I", "fecha": "17-03-2024"}
diccMision["mision10"] = {"lugar": "Ciudad J", "fecha": "22-03-2024"}




def registrar(mision, lugar, fecha):
    """Esta función registrará las misiones en el diccionario correspondiente con los datos:
        mision, lugar, fecha. Mision será la clave del diccionario."""
    if validarMision(mision) == True:
        fechaFormatoDate = convertir_a_fecha(fecha)
        fechaFormatoString = convertir_a_fechaString(fechaFormatoDate)
        diccMision[mision] = {"lugar": lugar, "fecha": fechaFormatoString}
        print("Mision registrada correctamente")
    else:
        print("Error: la mision introducida ya se encuentra registrada")
    



def esborrarMision(mision):
    """Esta función eliminará de la base de datos la mision introducida"""
    if validarMision(mision) == False:
        del diccMision[mision]
        print("Mision borrada de la base de datos correctamente")
    else:
        print("Error: la mision seleccionada no se encuentra en la base de datos")

def listAnyo(año):
    """Esta funcion listará las mision por año que estén en la base de datos"""
    if validarAnyo(año) == True:
        year = int(año)
        print(F"ANY {año}")
        contador = 0
        for x in diccMision:
            if convertir_a_fecha(diccMision[x]["fecha"]).year == year:
                print(diccMision[x]["fecha"], x)
                contador += 1
            
        if contador == 0:  
            print("No hay misiones registradas para este año")
    else:
        print("Error: no has introducido un año valido")




def setmana():
    """Esta función muestra todas las misiones que se registrarán en los siguientes 7 dias de la semana"""
    hoy = datetime.strftime(obtener_fecha_actual(),"%d-%m-%Y")


    hoy = datetime.strptime(hoy, '%d-%m-%Y')

    diccDias = {"0": "AVUI", "1": "DEMÀ", "2": "DEMÀ PASAT", "3": "EN TRES DIES", "4": "EN CUATRE DIES", "5": "EN CINC DIES",
                "6": "EN SIS DIES", "7": "EN SET DIES"}

    print("SETMANA")
    contador = 0
    for x in diccMision:
        fecha_mision = convertir_a_fecha(diccMision[x]["fecha"])
        dias_restantes = (fecha_mision - hoy).days
        if 0 <= dias_restantes <= 7:
            contador += 1
            if str(dias_restantes) in diccDias:
                print("=> * ",diccDias[str(dias_restantes)], " *")
                print(diccMision[x]["fecha"], x,diccMision[x]["lugar"])
            
    if contador == 0:
        print("No se encuentran misiones registradas para los siguientes 7 días")




def primera():
    """Esta funcion mostrará la primera misión registrada, indicando cuantos dias han pasado desde la fecha 
        o faltan, o si es hoy."""
    if not diccMision:
        print("Error: no hay misiones registradas")
    else: 

        min = None
        primera = ""
        for clave, valor in diccMision.items():
            for x , y in valor.items():
                if x == "fecha":
                    if min == None:
                        min = y
                        primera = clave
                    elif convertir_a_fecha(min) > convertir_a_fecha(y):
                        min = y
                        primera = clave
        # print(min,obtener_fecha_actual())
        diaspasados = (convertir_a_fecha(min) - obtener_fecha_actual()).days + 1
        print(f"La missio mes antiga es: {primera}")
        print("Lloc: ", diccMision[primera]["lugar"])
        print("Data:", diccMision[primera]["fecha"])
        if diaspasados > 0:
            print("Faltan: ", diaspasados, "dias")
        elif diaspasados < 0:
            diaspasados2 = diaspasados * -1
            print("Han pasado:", diaspasados2, "dias")
        elif diaspasados == 0:
            print("La mision es hoy")


def fechaMayorMenor(fecha1, fecha2):
    """esta funcion determina si la primera fecha introducida es mayor, menor o ="""

    if fecha1 < fecha2:
        return True
    
    elif fecha1 == fecha2:
        return "igual"
    
    elif fecha1 > fecha2:
        return False


def restarFechaHastaHoy(fecha):
    """Esta función determinará cuantos dias han pasado, si estamos en ese dia o quedan para que ocurra una fecha"""
    
    hoy = obtener_fecha_actual()
    if fecha < hoy:
        dias = (hoy - fecha).days
        return dias
    elif fecha == hoy:
        return True
    elif fecha > hoy:
        dias = (fecha - hoy).days
        return dias

def obtener_fecha_actual():
    fecha_actual = datetime.now()
    
    return fecha_actual


def validarAnyo(año):
    """Esta función validará que un valor introducido sea un int > 0"""

    if año.isdigit() == True:
        if int(año) > 0:
            return True
        else:
            return False
    else:
        return False




def validarMision(mision):
    """Esta función validará la existencia de una misión con la clave introducida"""
    if mision in diccMision:
        return False
    return True






def convertir_a_fechaString(fecha):
    fechaformato = datetime.strftime(fecha, "%d-%m-%Y")
    return fechaformato



def convertir_a_fecha(cadena_fecha):
    """Esta función convierte un string formato fecha a formato date"""
    fecha = datetime.strptime(cadena_fecha, "%d-%m-%Y")
    return fecha
# print(convertir_a_fecha("22-02-2024"))