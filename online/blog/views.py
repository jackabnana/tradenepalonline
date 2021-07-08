
from typing import ClassVar
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
# Create your views here.

def index (request):
    return render(request, 'index.html', {})

def about (request):
    return render(request, 'about.html', {})

class BlogView(ListView):
    model = Post
    template_name = 'blog.html'

class ArticleDetailView(DetailView):
    model =Post
    template_name = 'blog-single.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'