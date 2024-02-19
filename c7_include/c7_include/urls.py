
from django.urls import path
from channels import views

urlpatterns = [
    path('', views.index),
    path('company/',views.company,name = 'company'),
    path('school/',views.school,name = 'school')
]