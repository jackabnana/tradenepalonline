
from django.urls import path
from . import views
from .views import AddPostView, ArticleDetailView, CategoryView, UpdatePostView, DeletePostView, AddCategoryView


urlpatterns = [
   path('', views.index, name="home"),
   path('about/', views.about, name="about"),
   path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
   path('add_post/', AddPostView.as_view(), name="add_post"),
   path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
   path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
   path('add_category/', AddCategoryView.as_view(), name="add_category"),
   path('category/<str:cats>/', CategoryView, name='category'),

]
