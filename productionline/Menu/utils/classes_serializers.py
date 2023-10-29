class Bottle:

    def __init__(self, name: str = "bottle", 
                 begindate: str = "10/10/1999 12:00", 
                 enddate: str = "10/10/1999 12:00",
                 state: bool = True) -> None:
        
        self.name: str = name
        self.begindate: str = begindate
        self.enddate: str = enddate
        self.state: bool = state
    
    def set_date(self, begin: str, end: str) -> None:
        self.begindate = begin
        self.enddate = end
    
    def set_state(self, state: bool) -> None:
        self.state = state

class ProductionLine:
    
    def  __init__(self, name: str = "Default Plant", 
                  creation_date: str = "1/1/1999", 
                  bottles_processed: int = 0,
                  goodb: list[Bottle] = [],
                  badb: list[Bottle] = []) -> None:
        
        self.name: str = name
        self.creation_date: str = creation_date
        self.bottles_processed: int = bottles_processed
        self.goodbottles: list[Bottle] = []
        self.badbottles: list[Bottle] = []

    def add_bottle(self, n: str, beg: str, e: str, good: bool) -> None:
        b: Bottle = Bottle(n,beg,e,good)
        if good:
            self.goodbottles.append(b)
        else:
            self.badbottles.append(b)
    
    def add_bottles(self, bottles: list[Bottle], goods: list[bool]) -> None:
        for i in range(len(bottles)):
            if goods[i]:
                self.goodbottles.append(bottles[i])
            else:
                self.badbottles.append(bottles[i])
    def update_bottles_processed(self) -> None:
        self.bottles_processed = len(self.goodbottles) + len(self.badbottles)

class ProductionPlant:

    def __init__(self, name: str = "Default Line", 
                 creation_date: str = "11/09/1999", 
                 production_lines: list[ProductionLine] = []) -> None:

        self.name: str = name
        self.creation_date: str = creation_date
        self.production_lines: list[ProductionLine] = []
      
    def add_pline(self, pl: ProductionLine) -> None:
        self.production_lines.append(pl)
    