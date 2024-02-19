
from django.urls import path,include
from article import views

urlpatterns = [
    path('article/', include('article.urls'))
]
