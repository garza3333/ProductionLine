from typing import Any
from .classes_serializers import *
import json
import ast
import os

class JsonManager:

    def __init__(self) -> None:
        self.static_production_plants: list[ProductionPlant] = []
        self.static_production_lines: list[ProductionLine] = []

    def serialize_to_json(self, plant: ProductionPlant) -> str:
        
        data:dict[str, Any] = {
            "name": plant.name,
            "creation_date": plant.creation_date,
            "production_lines": []
        }
        
        for line in plant.production_lines:
            line_data:dict[str, Any] = {
                "name": line.name,
                "creation_date": line.creation_date,
                "bottles_processed": line.bottles_processed,
                "goodbottles": [b.__dict__ for b in line.goodbottles],
                "badbottles": [b.__dict__ for b in line.badbottles]
            }
            data["production_lines"].append(line_data)
        
        
        return json.dumps(data)

    def deserialize_from_json(self, json_str: str) -> ProductionPlant:
        data: Any = json.loads(json_str)
        
        
        plant = ProductionPlant(name=data["name"], creation_date=data["creation_date"])
        
        for line_data in data["production_lines"]:
            line = ProductionLine(
                name=line_data["name"],
                creation_date=line_data["creation_date"],
                bottles_processed=line_data["bottles_processed"]
            )
            
            goodbottles: list[Bottle] = [Bottle(**bottle_data) for bottle_data in line_data["goodbottles"]]
            badbottles: list[Bottle] = [Bottle(**bottle_data) for bottle_data in line_data["badbottles"]]
            
            line.goodbottles = goodbottles
            line.badbottles = badbottles
            plant.add_pline(line)
        
        return plant

    
    
    def save_db(self,file_path: str = "") -> None:
        fpath = file_path
        if fpath == "":
            fpath = "productionline/Menu/static/Menu/db/db.txt"
        else:
            db_path: str = os.path.join(os.getcwd(),"Menu/static/Menu/db")
            fpath: str = os.path.join(db_path,file_path)
        data: dict[str, Any] = {
            "production_plants": [self.serialize_to_json(p) for p in self.static_production_plants],
        }
        with open(fpath, "w") as file:
            file.write(str(data))
            file.close()
            print("DB saved")

    
    def load_db(self,file_path: str = "") -> None:
        fpath = file_path
        if fpath == "":
            fpath = "productionline/Menu/static/Menu/db/db.txt"
        else:
            db_path: str = os.path.join(os.getcwd(),"Menu/static/Menu/db")
            fpath: str = os.path.join(db_path,file_path)
        try:
            with open(fpath, "r") as file:
                data: dict[str, Any] = ast.literal_eval(file.read())
                self.static_production_plants = [self.deserialize_from_json(p) for p in data["production_plants"]]
                file.close()
                print("DB loaded")
        except FileNotFoundError:
            print("Coudn't load any information.")

    
    def add_pp_to_db(self,p: ProductionPlant) -> None:
        self.static_production_plants.append(p)

    
    def add_pp_to_db_l(self,plist: list[ProductionPlant]) -> None:
        for p in plist:
            self.static_production_plants.append(p)
    


# Feeling a few data to show in the website

# jm = JsonManager()

# p1 = ProductionPlant("Refrescos", "10/28/2023", [])
# p2 = ProductionPlant("Cerveza", "10/28/2023", [])
# p3 = ProductionPlant("Agua", "10/28/2023", [])

# pl1 = ProductionLine("Linea Llenadora 1","10/28/2023",0,[],[])
# pl2 = ProductionLine("Linea Llenadora 1","10/28/2023",0,[],[])
# pl3 = ProductionLine("Linea Llenadora 1","10/28/2023",0,[],[])

# p1.add_pline(pl1)
# p2.add_pline(pl2)
# p3.add_pline(pl3)


# jm.add_pp_to_db_l([p1,p2,p3])
# jm.save_db("")
# jm.load_db("")
# print(jm.static_production_plants[0].name)

