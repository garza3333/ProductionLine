jm = JsonManager()

p1 = ProductionPlant("Production Plant 1", "10/25/2023", [])
p2 = ProductionPlant("Production Plant 2", "10/25/2023", [])
p3 = ProductionPlant("Production Plant 3", "10/25/2023", [])

pl1 = ProductionLine("Production line 1","1/1/1999",0,[],[])
pl2 = ProductionLine("Production line 2","1/1/1999",0,[],[])
pl3 = ProductionLine("Production line 3","1/1/1999",0,[],[])


b1 = Bottle("Bottle1", "10/25/2023 12:00", "10/25/2023 12:00", True)
b2 = Bottle("Bottle1", "10/25/2023 12:00", "10/25/2023 12:00", False)
b3 = Bottle("Bottle1", "10/25/2023 12:00", "10/25/2023 12:00", True)

pl1.add_bottles([b1,b2,b3],[True,False,True])
pl2.add_bottle(b2,True)
pl3.add_bottles([b1,b3],[True,True])


p1.add_pline(pl1)
p1.add_pline(pl2)


p2.add_pline(pl3)

p3.add_pline(pl1)
p3.add_pline(pl2)
p3.add_pline(pl3)

jm.add_pp_to_db_l([p1,p2,p3])
jm.save_db("")