import requests as r
import json as js
def getrequest():
    url = "https://pokeapi.co/api/v2/pokemon/1/"
    response = r.get(url)
    if response.status_code == 200:
        datos = js.loads(response.text)
        print(js.dumps(datos, indent= 3))
    else:
        print("error api")

getrequest()