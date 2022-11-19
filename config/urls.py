from django.contrib import admin
from django.urls import path, include
from covid19 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
]
