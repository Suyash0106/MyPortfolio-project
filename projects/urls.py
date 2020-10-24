import django.urls
from projects import views

urlpatterns = [
    django.urls.path('', views.all_projects, name='allprojects'),
    django.urls.path('<int:blog_id>/', views.details, name='detail'),
]
