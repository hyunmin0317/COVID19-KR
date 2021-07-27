from django.urls import path
from . import views

app_name = 'covid19'

urlpatterns = [
    path('kr/', views.home, name='home'),
]
