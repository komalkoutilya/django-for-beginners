from django.shortcuts import render
from django.views.generic import ListView, DetailView # for 
from django.views.generic.edit import CreateView, UpdateView, DeleteView # for create, update and delete forms
from .models import Post
from django.urls import reverse_lazy
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

class BlogCreateView(CreateView):
    model=Post
    template_name="post_new.html"
    fields=['title', 'author', 'body']
    # Here we have to explicitly specify the fields that we want to collect via forms
    # Once the Django-form successfully submitted, default behaviour is to always redirect to get_absolute_url() of model specified.
    # If we don't want this to happen then we need to specify "success_url" in view.

class BlogUpdateView(UpdateView):
    model=Post
    template_name="post_edit.html"
    fields=['title', 'body']

class BlogDeleteView(DeleteView):
    model=Post
    template_name="post_delete.html"
    success_url=reverse_lazy("home")