from django.urls import path
from channels import views
from aggregate import views as aggregateView

urlpatterns = [
    # Basic query
    path('', views.index,name = 'index'),
    path('insert/',views.insert_article,name= 'insert'),
    path('edit/',views.edit_article,name= 'edit'),
    path('check/', views.check,name = 'check'),
    path('check2/', views.check2,name = 'check2'),
    path('check3/', views.check3,name = 'check3'),
 	path('check4/', views.check4,name = 'check4'),

    # Aggregate
    path('checkAggr/', aggregateView.checkAggr,name = 'checkAggr'),
    path('insertAggr/', aggregateView.insertAggr,name = 'insertAggr'),
    path('checkAvg/', aggregateView.checkAvg,name = 'checkAvg'),
    path('checkAnnotion/', aggregateView.checkAnnotion,name = 'checkAnnotion'),
    path('checkCount/', aggregateView.checkCount,name = 'checkCount'),
    path('checkMaxMin/', aggregateView.checkMaxMin,name = 'checkMaxMin'),
    path('checkSum/', aggregateView.checkSum,name = 'checkSum'),

    # QuerySet
    path('Ffunction/',aggregateView.Ffunction,name='Ffunction'),
    path('QFunction/',aggregateView.QFunction,name='QFunction'),
    path('excludeFunction/',aggregateView.excludeFunction,name='excludeFunction'),
    path('orderby/',aggregateView.orderby,name='orderby'),
    path('values/',aggregateView.values,name='values'),
    path('selectRelated/',aggregateView.selectRelated,name='selectRelated'),
    path('prefetchRelated/',aggregateView.prefetchRelated,name='prefetchRelated'),
    path('getFunction/',aggregateView.getFunction,name='getFunction'),
    path('createFunction/',aggregateView.createFunction,name='createFunction'),
    path('updateFunction/',aggregateView.updateFunction,name='updateFunction'),
    path('slice/',aggregateView.slice,name='slice'),
]