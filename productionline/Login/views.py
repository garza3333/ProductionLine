from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def login(request: HttpRequest) -> HttpResponse:
    context: dict[Any, Any] = {}
    return render(request,"login.html",context)

def signin(request: HttpRequest) -> HttpResponse:
    context: dict[Any, Any] = {}
    user: str = request.POST.get("name","default")
    password: str = request.POST.get("password","default")
    if(user == "admin" and password == "admin1234"):
        return render(request, "menu.html", context)
    else:
        return render(request, "login.html", context)

