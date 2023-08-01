from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog,Contacts,Footer #manager objects
from .forms import BlogForm

footer = Footer.objects.all()
def index(request):
    blog = Blog.objects.all()
    if request.GET:
        search_data = request.GET.get('search')
        if search_data != "":
            data = Blog.objects.filter(title__icontains=search_data)
            context = {"blogs":data, "footer":footer}
            return render(request, "migrations/index.html", context)
    return render(request, "migrations/index.html", {"blogs":blog, "footer":footer})

def about(request):
    return render(request, 'migrations/about.html', {"footer":footer})

def create(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("migrations:index")
    return render(request, 'migrations/createblog.html', {"form":form, "footer":footer})

def partData(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'migrations/post.html', {"blog":blog, "footer":footer})

def delete(request, id):
    print(id)
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect("migrations:index")

def update(request, id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect("migrations:index")
    return render(request, 'migrations/createblog.html', {"blog":blog, "footer":footer})

def contacts(request):
    if(request.method == "POST"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = Contacts(name=name, email=email)
        contact.save()
    return render(request, 'migrations/contactus.html', {"footer":footer})