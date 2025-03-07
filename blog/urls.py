from .views import bloglistview
from django.urls import path

urlpatterns = [
    path("", bloglistview, name="blog_list_view"),
]
