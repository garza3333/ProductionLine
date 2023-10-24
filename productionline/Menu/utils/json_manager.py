from typing import Any
from classes_serializers import *
import json

class JsonManager:

    static_production_plants: list[ProductionPlant] = []
    static_production_lines: list[ProductionLine] = []


    @staticmethod
    def serialize_production_line(production_line: ProductionLine)-> str:
        return json.dumps(production_line, default=lambda o: o.__dict__, indent=4)

    @staticmethod
    def deserialize_production_line(json_str: str) -> ProductionLine:
        data: Any = json.loads(json_str)
        return ProductionLine(**data)

    @staticmethod
    def serialize_production_plant(production_plant: ProductionPlant) -> str:
        data: dict[str, Any] = production_plant.__dict__
        data['production_lines'] = [line.__dict__ for line in data['production_lines']]
        return json.dumps(data)

    @staticmethod
    def deserialize_production_plant(json_str: str) -> ProductionPlant:
        data: Any = json.loads(json_str)
        data['production_lines'] = [ProductionLine(**line_data) for line_data in data['production_lines']]
        return ProductionPlant(**data)
    
    @staticmethod
    def save_db(file_path: str) -> None:
        # Guardar la información en un archivo JSON
        data: dict[str, Any] = {
            "production_plants": [plant.__dict__ for plant in JsonManager.static_production_plants],
            "production_lines": [line.__dict__ for line in JsonManager.static_production_lines]
        }
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_db(file_path: str) -> None:
        try:
            with open(file_path, "r") as file:
                data: Any = json.load(file)
                # Cargar las plantas y líneas desde el archivo
                JsonManager.static_production_plants = [ProductionPlant(**plant_data) for plant_data in data["production_plants"]]
                JsonManager.static_production_lines = [ProductionLine(**line_data) for line_data in data["production_lines"]]
        except FileNotFoundError:
            print("El archivo no existe. No se cargó ninguna información.")

    @staticmethod
    def add_pp_to_db(p: ProductionPlant) -> None:
        JsonManager.static_production_plants.append(p)

    @staticmethod
    def add_pp_to_db_l(plist: list[ProductionPlant]) -> None:
        for p in plist:
            JsonManager.static_production_plants.append(p)
    
    @staticmethod
    def add_pl_to_db(pl: ProductionLine) -> None:
        JsonManager.static_production_lines.append(pl)

    @staticmethod
    def add_pl_to_db_l(pllist: list[ProductionLine]) -> None:
        for pl in pllist:
            JsonManager.static_production_lines.append(pl)
    


# Feeling a few data to show in the website

p1 = ProductionPlant(name = "Production Plant 1")
p2 = ProductionPlant(name = "Production Plant 2")
p3 = ProductionPlant(name = "Production Plant 3")

pl1 = ProductionLine(name = "Production line 4")
pl2 = ProductionLine(name = "Production line 2")
pl3 = ProductionLine(name = "Production line 3")

p1.add_pline(pl1)
p1.add_pline(pl2)

p2.add_pline(pl3)

p3.add_pline(pl1)
p3.add_pline(pl2)
p3.add_pline(pl3)


