from django.contrib import admin
from django.urls import include,path
from Login.views import login

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("Login.urls"))
]
