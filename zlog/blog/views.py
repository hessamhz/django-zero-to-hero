from django.shortcuts import render, HttpResponse

# Create your views here.


def blog_view(request):
    return HttpResponse('hey')
