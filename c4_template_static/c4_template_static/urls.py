
from django.urls import path
from channels import views
from micro import views as micro_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('micro/',micro_views.micro)
] + static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS[0])
# Another way to add static files in your own folder

