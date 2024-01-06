import datetime

def avui():
    # Formato "Hoy es: 17 de Abril del 2022"
    return datetime.datetime.now().strftime("Hoy es: %d de %B del %Y")

def properAniversari(data_naixement):
    data_naixement = datetime.datetime.strptime(data_naixement, "%d/%m/%Y")
    avui = datetime.datetime.now()
    any_actual = avui.year
    proper_aniversari = datetime.datetime(year=any_actual, month=data_naixement.month, day=data_naixement.day)
    if proper_aniversari < avui:
        proper_aniversari = datetime.datetime(year=any_actual + 1, month=data_naixement.month, day=data_naixement.day)
    return proper_aniversari.strftime("%d/%m/%Y")

def quantFalta(data_futura):
    data_futura = datetime.datetime.strptime(data_futura, "%d/%m/%Y")
    avui = datetime.datetime.now()
    return (data_futura - avui).days

def aniversari(data):
    data = datetime.datetime.strptime(data, "%d/%m/%Y")
    mes_actual = datetime.datetime.now().month
    return data.month == mes_actual