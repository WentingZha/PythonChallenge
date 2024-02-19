
from django.urls import path
from front import views

urlpatterns = [
    path('', views.index),
    path('slice/', views.slice_view),
    path('striptags/', views.striptags_view),
    path('truncatechars/', views.truncatechars_view)
]

