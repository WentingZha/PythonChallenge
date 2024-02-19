
from django.urls import path,include

urlpatterns = [
    path('article/',include('article.urls'))
]
