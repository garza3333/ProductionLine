from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from Menu.utils.json_manager import JsonManager
from django.http import JsonResponse
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time

# Global Variables

global jm
jm = JsonManager()

def login(request: HttpRequest) -> HttpResponse:
    context: dict[Any, Any] = {}
    return render(request,"login.html",context)

def signin(request: HttpRequest) -> HttpResponse:
    global jm
    context: dict[Any, Any] = {}
    user: str = request.POST.get("name","default")
    password: str = request.POST.get("password","default")
    if(user == "admin" and password == "admin1234"):
        jm.load_db("db.txt")
        context["db"] = jm.static_production_plants
        print(len(jm.static_production_plants))
        print(len(jm.static_production_plants[0].production_lines))
        print(len(jm.static_production_plants[1].production_lines))
        print(len(jm.static_production_plants[2].production_lines))
        print(len(jm.static_production_plants[0].production_lines[0].goodbottles))
        print(len(jm.static_production_plants[0].production_lines[0].badbottles))
        return render(request, "menu.html", context)
    else:
        return render(request, "login.html", context)
    
def get_p_lines_names(request: HttpRequest, plantname: str) -> JsonResponse:
    global jm
    data: dict[str, str] = {}
    
    for p in jm.static_production_plants:
        if p.name == plantname:
            cont = 1
            for pl in p.production_lines:
                data["plant"+str(cont)] = pl.name
                cont+=1
    return JsonResponse(data)

def get_p_lines_data(request: HttpRequest, plname: str) -> JsonResponse:
    global jm
    data: dict[str, Any] = {}
    jm.load_db("db.txt")
    print(request.GET)

    beg: Any = request.GET["beg"]
    end: Any = request.GET["end"]
    pname: Any = request.GET["pplant"]
    begin_date: datetime = datetime.strptime(beg, "%m-%d-%Y %H:%M")
    end_date: datetime = datetime.strptime(end, "%m-%d-%Y %H:%M")
    
    
    
    for p in jm.static_production_plants:
        if p.name == pname:
            for pl in p.production_lines:
                if pl.name == plname:
                    cont = 1
                    for b in pl.goodbottles:
                        bottle_date: datetime = datetime.strptime(b.enddate, "%m/%d/%Y %H:%M")
                        if begin_date <= bottle_date <= end_date:
                            data["product"+str(cont)] = [b.name,b.enddate,b.state]
                            cont+=1
                    for b in pl.badbottles:
                        bottle_date: datetime = datetime.strptime(b.enddate, "%m/%d/%Y %H:%M")
                        if begin_date <= bottle_date <= end_date:
                            data["product"+str(cont)] = [b.name,b.enddate,b.state]
                            cont+=1

    return JsonResponse(data)

@csrf_exempt
def add_product(request: HttpRequest) -> JsonResponse:
    
    if request.method == 'POST':

        global jm
        jm.load_db("db.txt")
        
        pplant: str = request.POST.get("pplant","nothing")
        pline: str = request.POST.get("pline","nothing")
        name: str = request.POST.get("name","nothing")
        begindate: str = request.POST.get("begindate","01/01/2023 12:00")
        enddate: str = request.POST.get("enddate","01/01/2023 12:00")
        s : str = request.POST.get("state","false")
        state: bool = False
        if s == "true":
            state = True

        print(pplant,pline,name,begindate,enddate,state)
        
        for p in jm.static_production_plants:
            if p.name == pplant:
                print("TRUE PLANT")
                print(p.name, pplant)
                for l in p.production_lines:
                    if l.name == pline:
                        print("TRUE LINE")
                        print(l.name, pline)
                        l.add_bottle(name,begindate,enddate,state)
                        if l.goodbottles != []:
                            print(l.goodbottles[0])
                        if l.badbottles != []:
                            print(l.badbottles[0])
                        
                        jm.save_db("db.txt")
                        jm.load_db("db.txt")
                        time.sleep(0.2)
                        break

        return JsonResponse({'status': '201'})
    
    return JsonResponse({'status': '401'})

