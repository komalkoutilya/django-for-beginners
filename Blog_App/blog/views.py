from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.

class BlogListView(ListView):
    model=Post
    template_name="home.html"

class BlogDetailView(DetailView):
    model=Post
    template_name="post_detail_view.html"
    context_object_name="komal"
    # if you don't mention context_object_name simply use {{object}} or {{post}} smallercase of model name
    # if you use context_object_name then you can use either {{object}} or {{context_object_name_value}} i.e {{komal}}
    