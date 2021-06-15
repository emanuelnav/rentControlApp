from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('departamento/<str:pk>/',views.departamento, name="departamento"),
    path('cargarinquilino',views.cargarInquilino, name="cargarInquilino"),
    path('cargardepartamento',views.cargarDepartamento, name="cargarDepartamento"),
    path('inquilinos',views.inquilino, name="inquilinos"),
]