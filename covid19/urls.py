from django.urls import path
from .views import DetailAPI

urlpatterns = [
    path('<str:date>/', DetailAPI.as_view()),
]