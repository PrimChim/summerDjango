from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog,Contacts #manager objects
from .forms import BlogForm

def index(request):
    blog = Blog.objects.all()
    

    return render(request, "migrations/index.html", {"blogs":blog})

def about(request):
    return render(request, 'migrations/about.html')

def create(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, 'migrations/create.html', {"form":form})

def partData(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'migrations/index.html', {"blog":blog})

def delete(request, id):
    print(id)
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect("index")

def update(request, id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, 'migrations/create.html', {"form":form})

def contacts(request):
    if(request.method == "POST"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = Contacts(name=name, email=email)
        contact.save()
    return render(request, 'migrations/contactus.html')