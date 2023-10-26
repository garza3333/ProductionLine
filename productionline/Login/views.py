from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from Menu.utils.json_manager import JsonManager
from django.http import JsonResponse
from datetime import datetime

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

    print(request.GET)

    beg: Any = request.GET["beg"]
    end: Any = request.GET["end"]
    begin_date: datetime = datetime.strptime(beg, "%m-%d-%Y %H:%M")
    end_date: datetime = datetime.strptime(end, "%m-%d-%Y %H:%M")
    
    
    
    for p in jm.static_production_plants:
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
