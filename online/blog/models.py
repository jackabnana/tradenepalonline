from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        #return reverse('article-detail', args=(str(self.id))),
        return reverse('blog')


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255,default="tradebulletin")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    post_date = models.DateField(auto_now_add='True')
    category = models.CharField(max_length=255, default='uncategorised')
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    #image = models.ImageField(upload_to="media/", blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        #return reverse('article-detail', args=(str(self.id))),
        return reverse('blog')

