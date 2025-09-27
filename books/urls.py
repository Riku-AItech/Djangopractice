from django.urls import path
from . import views

urlpatterns = [
    path('api/get-title/', views.get_title, name='get_title'),
]