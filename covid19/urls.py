from django.urls import path
from .views import ListAPI

urlpatterns = [
    path('<int:year>/<int:month>/<int:day>/', ListAPI.as_view()),
]