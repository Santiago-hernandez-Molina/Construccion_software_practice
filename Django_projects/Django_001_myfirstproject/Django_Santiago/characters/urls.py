from django.urls import path
from .import views

app_name = 'characters'

urlpatterns = [
    path('', views.list, name="list_characters"),
    path('save', views.save, name="save_characters"),
    path('detail/<int:id>/', views.detail, name="detail_character"),
    path('filter_by_universe/<int:id>/', views.filter_by_universe, name="filter_by_universe"),
    path('puntouno',views.puntouno,name="puntouno"),
    path('puntodos',views.puntodos,name="puntodos"),
    path('puntotres',views.puntotres,name="puntotres"),
    path('puntocinco',views.puntocinco,name="puntocinco"),
    path('puntoseis',views.puntoseis,name="puntoseis"),
    path('puntosiete',views.puntosiete,name="puntosiete"),
    path('puntoocho',views.puntoocho,name="puntoocho"),
    path('puntonueve',views.puntonueve,name="puntonueve"),
    path('puntodiez',views.puntodiez,name="puntodiez"),
    path("prueba", views.list_universes, name="a"),

]
