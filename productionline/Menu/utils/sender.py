from typing import Any
import requests
from datetime import datetime


class Sender:
    def __init__(self) -> None:
        self.url = "http://127.0.0.1:8000/addProduct/"
    
    def send_product(self, pplant: str, pline: str, name: str, state: str)-> None:

        now: datetime = datetime.now()
        formatted_date: str = now.strftime("%m/%d/%Y %H:%M")

        data: dict[str, Any] = {
                "pplant": pplant,
                "pline": pline,
                "name": name,
                "begindate": formatted_date,
                "enddate": formatted_date,
                "state": state
            }
        
        response: requests.Response = requests.post(self.url, data=data)

        if response.status_code == 200:
            print("Solicitud POST exitosa.")
            print("Respuesta del servidor:")
            print(response.text)
        else:
            print("Error en la solicitud POST. Código de estado:", response.status_code)
            print("Contenido de la respuesta:")
            print(response.text)

s = Sender()
s.send_product("Refrescos", "Linea Llenadora 1", "Juice Bottle 1", "true")
s.send_product("Cerveza", "Linea Llenadora 1", "Beer Bottle 1", "false")
s.send_product("Agua", "Linea Llenadora 1", "Watter Bottle 1", "false")






