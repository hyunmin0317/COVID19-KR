from django.urls import path
from .views import DetailAPI, AllAPI

urlpatterns = [
    path('all/', AllAPI.as_view()),
    path('<str:date>/', DetailAPI.as_view()),
]