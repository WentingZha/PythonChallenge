from django.urls import path
from channels import views


# XSS attack means user submit some codes to get the information or change the website
# For example user submit '<script>alert('Hi Guard');</script>' as a comment
# But it trigger the JS code and pop up an alert

# Example 2: User post a comment <span style='color:red;'>Red Font</span>

urlpatterns = [
	path('', views.index,name = 'index'),
    path('createComment/', views.createComment,name='createComment'),
]
