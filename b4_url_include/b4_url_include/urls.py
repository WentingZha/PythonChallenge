
from django.urls import path,include
from movie import views

urlpatterns = [
    path('book/',include('book.urls','book')),
    path('movie/',include([
    	path('',views.movie),
    	path('list/',views.movie_list)
    	]))
]
