from django.urls import path
from App_coder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('villaolimpica/', views.villa_olimpica, name="Villa_Olimpica"),
    path('disciplina/', views.disciplina, name="Disciplina"),
    path('deportista/', views.deportista, name="Deportista"),
    path('villa_olimpica_form/', views.villa_olimpica, name="Villa_Olimpica_Form"),
    path('disciplina_form/', views.disciplina, name="Disciplina_form"),
    path('deportista_form/', views.deportista, name="Deportista_form"),
    path('busqueda/', views.busqueda),
]
