import requests
import json
import sys
import calendar

def dirección(argumentos):
    datos = argumentos.split("-")
    if len(datos) == 2:
        year = int(datos[0])
        mounth = int(datos[1])
        diaSemana , diasMes = calendar.monthrange(year, mounth)
        print("Parametros correctos")
        url = "https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.0012&start_date=2022-11-01&end_date=2022-12-31&daily=temperature_2m_max,temperature_2m_min,rain_sum&timezone=Europe%2FBerlin"
        url2 = f"https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.0012&start_date={datos[0]}-{datos[1]}-01&end_date={datos[0]}-{datos[1]}-{str(diasMes)}&daily=temperature_2m_max,temperature_2m_min,rain_sum&timezone=Europe%2FBerlin"

        response = requests.get(url2)
        # temperaturaMáxima = None
        # temperaturaMinima = None
        # diasLluvia = 0


                
                
        if response.status_code == 200:
            datos = json.loads(response.text)
            temperaturaMáxima = None
            temperaturaMinima = None
            diasLluvia = 0

            print(json.dumps(datos, indent=3))
            for x , y in datos["daily"].items():
                # if x == "time":
                #     for a in y:
                        

                if x == "temperature_2m_max":
                    for a in y:
                        if temperaturaMáxima is None or a > temperaturaMáxima:
                            temperaturaMáxima = a
                elif x == "temperature_2m_min":
                    for a in y:
                        if temperaturaMinima is None or a < temperaturaMinima:
                            temperaturaMinima = a
                elif x == "rain_sum":
                    for a in y:
                        if a > 0.1:
                            diasLluvia += 1
            print (f"Tmax= {temperaturaMáxima} ºC Tmin= {temperaturaMinima} ºC Dies de pluja: {diasLluvia}")


            print()
        else:
            print("Error al obtener datos de API")
    else:
        print("Parametros introducidos incorrectos")

argumentos = sys.argv
# argumentos = ["0", "2022-12"]
dirección(argumentos[1])
