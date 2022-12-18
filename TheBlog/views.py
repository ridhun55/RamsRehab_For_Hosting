from django.urls.base import reverse
from django.urls import reverse_lazy,reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, request

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from TheBlog.models import Category, Post, Comment
from TheBlog.forms import PostForm, CommentForm, EditForm, CategoryForm


class BlogHomeView(ListView):
   model = Post
   template_name = 'blogs/blog_home.html'
   cats = Category.objects.all()
   ordering = ['-post_date']
   
   def get_context_data(self, *args, **kwargs):
      cat_menu = Category.objects.all()
      context = super(BlogHomeView, self).get_context_data(*args, **kwargs)
      context["cat_menu"] = cat_menu
      return context
   

class ArticleView(DetailView):
   model = Post
   template_name = 'blogs/article.html'
   
   def get_context_data(self, *args, **kwargs):
      cat_menu = Category.objects.all()
      context = super(ArticleView, self).get_context_data(*args, **kwargs)
      
      stuff = get_object_or_404(Post, id=self.kwargs['pk'])
      total_likes = stuff.total_likes()
      
      liked = False
      if stuff.likes.filter(id=self.request.user.id).exists():
         liked = True
         
      context["cat_menu"] = cat_menu
      context["total_likes"] = total_likes
      context["liked"] = liked
      return context


def CategoryView(request, cats):
   category_posts = Post.objects.filter(category=cats.replace('-',' '))
   return render(request, 'blogs/blog_by_category.html', {'cats':cats.title().replace('-',' '), 'category_posts':category_posts})



class AddPostView(CreateView):
   model = Post
   form_class = PostForm
   template_name = 'blogs/blog_add_post.html'
   success_url = reverse_lazy('blog_home')


class AddCategoryView(CreateView):
   model = Category
   form_class = CategoryForm
   template_name = 'blogs/blog_add_category.html'
   # fields = '__all__'
   
   def get_context_data(self, *args, **kwargs):
      cat_menu_list = Category.objects.all()
      context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
      context["cat_menu_list"] = cat_menu_list
      return context
   success_url = reverse_lazy('add_category')


class AddCommentView(CreateView):
   model = Comment
   form_class = CommentForm
   template_name = 'blogs/blog_add_comment.html'
   
   def form_valid(self, form):
      form.instance.post_id = self.kwargs['pk']
      return super().form_valid(form)
   success_url = reverse_lazy('blog_home')


class EditPostView(UpdateView):
   model = Post
   form_class = EditForm
   template_name = 'blogs/blog_edit_post.html'
   success_url = reverse_lazy('blog_home')

   
class DeletePostView(DeleteView):
   model = Post
   template_name = 'blogs/blog_delete_post.html'
   success_url = reverse_lazy('blog_home')


def SearchPageView(request):
   if request.method == 'POST':
      searched = request.POST['searched']
      search_post = Post.objects.filter(title__icontains=searched)
      search_category = Post.objects.filter(category__icontains=searched)
      
      return render(request, 'blogs/search_page.html', {
         'searched':searched, 
         'search_post':search_post, 
         'search_category':search_category
         })
   else:    
      return render(request, 'blogs/search_page.html', {})