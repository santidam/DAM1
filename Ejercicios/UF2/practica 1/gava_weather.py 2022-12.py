import requests
import json

url = "https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.0012&start_date=2022-12-01&end_date=2022-12-31&daily=temperature_2m_max,temperature_2m_min,rain_sum&timezone=Europe%2FBerlin"

response = requests.get(url)
datos = json.loads(response.text)


if response.status_code == 200:
    print(json.dumps(datos, indent=3))

print()