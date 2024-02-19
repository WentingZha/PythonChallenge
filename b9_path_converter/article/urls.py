
from django.urls import re_path,path
from . import views


urlpatterns = [
    path('', views.article),
    # regular expression
    # \w:0-9,a-z,A-Z
    # +:one or more
    # \+: string"+"

    # Use the following paths to get the articles related with python
    # list/python \w
    # list/python+django \w+\+\w+
    # list/python+django+flask
    #re_path('list/(?P<category>\w+|(\w+\+\w+)+)/', views.article_list),

    # Url converter, http://127.0.0.1:8000/article/list/python+django+flask/
    path("list/<categ:category>/",views.article_list),
    path('detail/<int:article_id>/',views.article_detail, name='detail')
]

