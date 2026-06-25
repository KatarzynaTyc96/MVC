from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ksiazek, name='lista_ksiazek'),
    path('ksiazki/dodaj/', views.dodaj_ksiazke, name='dodaj_ksiazke'),
    path('ksiazki/<int:pk>/', views.szczegoly_ksiazki, name='szczegoly_ksiazki'),
    path('ksiazki/<int:pk>/edytuj/', views.edytuj_ksiazke, name='edytuj_ksiazke'),
    path('ksiazki/<int:pk>/usun/', views.usun_ksiazke, name='usun_ksiazke'),
]
