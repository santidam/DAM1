import requests
import json

url = "https://www.el-tiempo.net/api/json/v1/provincias/08/municipios/08089/weather"
url2 = "https://www.eltiempo.es/gava.html"
response = requests.get(url)
response2 = requests.get(url2)
# if response.status_code == 200:
#    print("Contenido:\n", response.text)
# data = response.json()
# print(data)
if response2.status_code == 200:
    #    print("Contenido:\n", response2.text)
    data = response.json()
    print(data)
