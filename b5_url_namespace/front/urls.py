from django.urls import path
from . import views

#the variable of namespace is app_name
app_name = 'front'

urlpatterns = [
    path('', views.index,name = 'index'),
    #path('login/',views.login)

    #mapping the name to signin, reverse the mapping in front/views.py
    path('signin/',views.login,name='login')
]
