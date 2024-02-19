
from django.urls import path
from ZwtLibrary import views

urlpatterns = [
    path('', views.index,name = 'index'),
    path('home/', views.add_book,name = 'home'),
    path('addBook/', views.add_book,name = 'addBook'),
    path('bookDetail/', views.book_detail, name = 'bookDetail'),
    path('bestSeller/', views.best_seller, name = 'bestSeller'),
    path('editBook/', views.edit_book, name = 'editBook'),
    path('user/', views.user, name = 'user')
]