class ProductionLine:
    
    def  __init__(self, name: str = "Default Plant", creation_date: str = "1/1/1999", bottles_processed: int = 0) -> None:
        self.name: str = name
        self.creation_date: str = creation_date
        self.bottles_processed: int = bottles_processed

class ProductionPlant:

    def __init__(self, name: str = "Default Line", creation_date: str = "11/09/1999", production_lines: list[ProductionLine] = []) -> None:

        self.name: str = name
        self.creation_date: str = creation_date
        self.production_lines: list[ProductionLine] = production_lines
      
    def add_pline(self, pl: ProductionLine) -> None:
        self.production_lines.append(pl)
    