from django.urls import URLPattern, path
from . import views

urlpatterns: list[URLPattern] = [
    path('', views.login, name='pl_login'),
    path('signin/', views.signin, name='signin'),
]
