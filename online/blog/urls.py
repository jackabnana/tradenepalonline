
from django.urls import path
from . import views
from .views import AddPostView, ArticleDetailView


urlpatterns = [
   path('', views.index, name="home"),
   path('about/', views.about, name="about"),
   path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
   path('add_post/', AddPostView.as_view(), name="add_post"),
]
