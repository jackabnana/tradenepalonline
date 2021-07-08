from blog.models import Post
from typing import ClassVar
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.

def index (request):
    return render(request, 'index.html', {})

class BlogView(ListView):
    model = Post
    template_name = 'blog.html'
