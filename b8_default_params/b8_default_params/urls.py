from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('page/<int:page>/', views.books),
]
