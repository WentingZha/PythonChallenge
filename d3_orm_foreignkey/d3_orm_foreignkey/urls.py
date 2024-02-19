from django.urls import path
from article import views

urlpatterns = [
    path('', views.index,name = 'index'),
    path('delete/<categoryId>',views.delete_view,name= 'delete'),
    path('insert/',views.insert_view,name= 'insert'),
    path('oneToMany/',views.one_to_many_view,name= 'oneToMany'),
    path('addObjectToList/',views.add_object_to_list,name= 'addObjectToList'),
    path('oneToOne/',views.one_to_one_view,name= 'oneToOne'),
    path('manyToMany/',views.many_to_many_view,name= 'manyToMany'),
]