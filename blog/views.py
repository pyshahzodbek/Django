from django.http import Http404
from django.views.generic import ListView, DetailView

# from django.shortcuts import render,get_object_or_404
from .models import Blog
#
# def bloglistview(request):
#     blogs = Blog.objects.all()
#     return render(request, "home.html", {"blogs": blogs})
#
#
# def blogdetailview(request,id):
#     blog=get_object_or_404(Blog,id=id)
#     context={
#         "blog":blog
#     }
#
#     return render(request,"blog_detail.html",context=context)
class BlogListView(ListView):
    model =Blog
    template_name = "home.html"
    context_object_name = "blogs"
class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog_detail.html"