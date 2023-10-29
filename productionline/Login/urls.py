from django.urls import URLPattern, path
from . import views

urlpatterns: list[URLPattern] = [
    path('', views.login, name='pl_login'),
    path('signin/', views.signin, name='signin'),
    path('getlinesnames/<str:plantname>', views.get_p_lines_names, name='getlinesnames'),
    path('getlinesdata/<str:plname>', views.get_p_lines_data, name='getlinesdata'),
    path('addProduct/', views.add_product, name='addProduct'),
]
