from django.urls import path
from .import views

app_name = 'characters'

urlpatterns = [
    path('', views.list, name="list_characters"),
    path('save', views.save, name="save_characters"),
    path('detail', views.detail, name="detail_characters"),
]
