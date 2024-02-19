from django.urls import path
from . import views

urlpatterns = [
    path('iftag/', views.iftag),
    path('fortag/', views.fortag),
    path('withtag/', views.withtag),

    path('urlTag/', views.urlTag),
    path('reading/', views.reading,name = 'reading'),
    path('news/', views.news,name = 'news'),
    path('boardGame/', views.boardGame,name='boardGame'),
    path('reading/detail/<book_id>', views.book_detail,name='bookDetail'),
    path('reading/category/<book_id>/<category_id>', views.book_category,name='bookCategory'),
 	path('login/', views.login,name = 'login'),

 	path('autoEscape/', views.autoEscape),
 	path('verbatimTag/', views.verbatimTag)
]

