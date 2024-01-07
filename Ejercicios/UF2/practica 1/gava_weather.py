import requests
import json
import sys
if "-" in sys.argv:
    datos = argv.split("-")
    if len(datos) > 1 and len(datos) <= 2:
        print("Parametros correctos")
        url = "https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.0012&start_date=2022-12-01&end_date=2022-12-31&daily=temperature_2m_max,temperature_2m_min,rain_sum&timezone=Europe%2FBerlin"
        url2 = f"https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.0012&start_date={datos[0]}-{datos[1]}-01&end_date={datos[0]}-{datos[1]}-31&daily=temperature_2m_max,temperature_2m_min,rain_sum&timezone=Europe%2FBerlin"

        response = requests.get(url2)
        datos = json.loads(response.text)

        if response.status_code == 200:
            print(json.dumps(datos, indent=3))

        print()
    else:
        print("Cantidad de datos introducidos incorrectos")
else:
    print("Parametros introducidos incorrectos")
