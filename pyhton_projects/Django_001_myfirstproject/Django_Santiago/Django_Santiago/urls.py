from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('characters/',include('characters.urls',namespace="characters")),
]
