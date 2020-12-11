from django.urls import path
from .views import RegisterApi

urlpatterns = [
    path('api/register', RegisterApi.as_view(), name='register'),
]
