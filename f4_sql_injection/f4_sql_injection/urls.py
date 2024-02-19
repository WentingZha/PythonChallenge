from django.urls import path
from wing import views

urlpatterns = [
    path('', views.home,name = 'home'),
    path('getAnimalByName/', views.getAnimalByName,name = 'getAnimalByName'),
]
