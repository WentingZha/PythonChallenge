from django.urls import path
from channels import views

urlpatterns = [
    path('', views.channels,name='channels'),
    path('addChannel/', views.addChannel,name='addChannel'),
    path('httpResponse/',views.httpResponse,name='httpResponse'),
    path('jsonResponse/',views.jsonResponse,name='jsonResponse'),
    path('csvView/',views.csvView,name='csvView'),
    path('csvTemplate/',views.csvTemplate,name='csvTemplate'),
    path('largeCsvFile/',views.largeCsvFile,name='largeCsvFile'),
    
]
