from django.shortcuts import render, HttpResponse
from .models import BlogPost
# Create your views here.


def blog_view(request):
    queryset = BlogPost.objects.filter(target_age='E')
    return render(request, 'posts.html', context={'posts': queryset})
