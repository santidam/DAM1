from datetime import datetime, timedelta, date

def fechaFormatoDate(string):
    """esta función convierte un string a formate date time"""

    date =  datetime.strptime(string, "%d/%m/%Y")
    # dateString = datetime.strftime(date, "El día es %d de %m del %Y")
    # print(dateString)
    
    return date

def restarFecha(fecha1, fecha2):
    """ Esta funcion resta """
    fechaFinal = fecha1 - fecha2
    print(fechaFinal)


# fechaFormatoDate("22/03/2023")

def avui():
    """Esta función determina la fecha actual """

    fecha = datetime.strptime(datetime.now(),)
    dia = fecha.day
    mes = fecha.month
    año = fecha.year
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
             "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    
    print(f"Hoy es: {dia} de {meses[mes-1].capitalize()} del {año} ")
    return fecha

def properAniversari(dataString):
    """aquesta funció rep la data de naixement en una cadena 
        amb format “dia/mes/any” i retorna la data del proper
        aniversari."""
    cumpleaños = datetime.strptime(dataString, "%d/%m/%Y" )
    proximoCumpleaños = cumpleaños + timedelta(days = 365)
    print(proximoCumpleaños)
    return proximoCumpleaños
#properAniversari("01/02/2024")


def cuantFalta(dataString):
    """ aquesta funció rep una data, del futur, i ha de retornar quants 
        dies falten per a que arribi la data."""
    
    data = fechaFormatoDate(dataString)
    dataToday = datetime.now()
    if data > dataToday:
        diferencia = data - dataToday
        return diferencia.days
    else:
        print("Error la fecha proporcionada debe ser posterior a la actual")

def aniversari(dataString):
    """aquesta funció rep una cadena amb format “dia/mes/any” i ha 
    de retornar un booleà indicant si el mes que sha donat com argument 
    coincideix amb el mes actual"""

    data = fechaFormatoDate(dataString)
    if data.month == datetime.now().month:
        return True
    return False




# #avui()
# fecha = date.today()

# print(cuantFalta("02/03/2024"))

# print(aniversari("02/02/2024"))