
from typing import ClassVar
from django import forms
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, EditForm
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
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update.html'
    #fields = ['title', 'title_tag', 'body']