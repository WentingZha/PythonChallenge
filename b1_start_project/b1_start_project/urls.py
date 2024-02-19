from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from book.views import book
from movie.views import movie

def index(request):
	return HttpResponse("Home Page")


urlpatterns = [
    path('admin/', admin.site.urls),
    #http://127.0.0.1:8000
    path('',index),
    #http://127.0.0.1:8000/book/
    path('book/',book)
]
