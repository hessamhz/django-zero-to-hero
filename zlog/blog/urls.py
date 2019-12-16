from django.urls import path
from .views import blog_view

urlpatterns = [
    path('posts/', blog_view, name='blog_posts'),
]
