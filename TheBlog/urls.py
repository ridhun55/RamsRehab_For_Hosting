from django.contrib import admin
from django.urls import path
from TheBlog.views import BlogHomeView, ArticleView, CategoryView
from TheBlog.views import AddPostView, AddCommentView, AddCategoryView
from TheBlog.views import EditPostView, DeletePostView, SearchPageView

#  ================== LOGIN Urls.py =========================

# from django import views
# from .views import UserRegisterView,  PasswordsChangeView
# from django.contrib.auth import views as auth_views
# from . import views

urlpatterns = [
    path('', BlogHomeView.as_view(), name="blog_home"),
    path('article/<int:pk>', ArticleView.as_view(), name="article"),
    path('category/<str:cats>/', CategoryView, name="category"),

    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),

    path('article/edit/<int:pk>', EditPostView.as_view(), name="edit_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),

    path('search_page/', SearchPageView, name="search_page"),


]