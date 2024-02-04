from datetime import datetime, timedelta, date

def fechaFormatoDate(fecha):
    """esta función convierte un string a formate date time"""

    date =  datetime.strptime(fecha, "%d/%m/%Y")
    dateString = datetime.strftime(date, "El día es %d de %m del %Y")
    print(dateString)
    
    return date

def fechaFormatoString(fecha):
    """ Convierte una fecha en formato Datetime a formato String"""
    date = datetime.strftime(fecha, "%d/%m/%Y")
    return date
    

def restarFecha(fecha1, fecha2):
    """ Esta función resta dos fechas en formato date """
    fechaFinal = fecha1 - fecha2
    print(fechaFinal)