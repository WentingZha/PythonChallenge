from django.urls import path
from . import views

urlpatterns = [
	path('', views.channels),
    path('transfer/', views.transfer,name='transfer'),
]
