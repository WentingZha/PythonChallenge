from django.urls import path
from channels import views

urlpatterns = [
    path('index/', views.index, name = 'index'),
]
