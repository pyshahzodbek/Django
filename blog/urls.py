from .views import BlogListView, BlogDetailView
from django.urls import path

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list_view"),
    path("blogs/<int:pk>/",BlogDetailView.as_view(),name="blog_detail"),
]
