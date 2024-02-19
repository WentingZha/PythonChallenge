
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/',views.add_view),
    path('cut/',views.cut_view),
    path('date/',views.date_view),
    path('default/',views.default_view),
    path('first/',views.first_view),
    path('floatformat/',views.floatformat_view),
    path('join/',views.join_view),
    path('random/',views.random_view),
    path('safe/',views.safe_view),
    path('slice/',views.slice_view),
    path('striptags/',views.striptags_view),
    path('truncatechars/',views.truncatechars_view)
] 