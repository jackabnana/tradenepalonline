
from typing import ClassVar
from django import forms
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
# Create your views here.

def index (request):
    return render(request, 'index.html', {})

def about (request):
    return render(request, 'about.html', {})

def CategoryView (request, cats):
    category_posts = Post.objects.filter(category=cats),
    return render(request, 'categories.html', {'cats':cats, 'category_posts':category_posts})

class BlogView(ListView):
    model = Post
    template_name = 'blog.html'
    ordering = ['-id']
    #ordering = ['-post_date']

class ArticleDetailView(DetailView):
    model =Post
    template_name = 'blog-single.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update.html'
    #fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog')
   