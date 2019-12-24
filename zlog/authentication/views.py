from django.shortcuts import render, redirect

# Create your views here.


def login_view(request):
    return redirect("blog_posts")
