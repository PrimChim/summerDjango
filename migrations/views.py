from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog #manager objects

def index(request):
    blog = Blog.objects.all()
    

    return render(request, "migrations/index.html", {"blogs":blog})

def about(request):
    return render(request, 'migrations/about.html')