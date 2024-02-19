
from django.urls import path
from wing import views

urlpatterns = [
	path('', views.channels,name='channels'),
    path('get_animals/', views.get_animals,name='get_animals'),
    path('add_animal/', views.add_animal,name='add_animal'),
    path('register/',views.register,name='register'),
    path('signin/',views.signin,name='signin')
]
