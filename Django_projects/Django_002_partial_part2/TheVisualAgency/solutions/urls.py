from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'solutions'
urlpatterns = [
    path('', views.list, name="list"),
    path('saveCategory', views.saveCategory, name="saveCategory"),
    path('detail/<int:id>/', views.detail, name="detail_category"),
]