from django.shortcuts import render
from .models import Blog

def bloglistview(request):
    blogs = Blog.objects.all()
    return render(request, "home.html", {"blogs": blogs})




