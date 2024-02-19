from django.urls import path,include

urlpatterns = [
    path('', include('front.urls')),
    path('cms/', include('cms.urls'))
]
