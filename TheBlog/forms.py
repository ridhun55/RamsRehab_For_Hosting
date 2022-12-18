from django import forms
from django.db import models
from django.forms import widgets
from TheBlog.models import Comment, Post, Category



choices = Category.objects.all().values_list('name','name')
choice_list = []

for item in choices:
         choice_list.append(item)

class PostForm(forms.ModelForm):
      
   class Meta:
      model = Post
      fields = ('title', 'title_tag', 'author', 'category', 'body','snippet', 'header_image')
      
      widgets = {
         'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Blog Title'}),
         'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder':'Blog Title Tag'}),
         'author': forms.TextInput(attrs={'class':'form-control','value':'', 'id':'dev','type':'hidden'}),
         # 'author': forms.Select(attrs={'class':'form-control'}),
         'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
         'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Blog content type here...'}),
         'snippet': forms.Textarea(attrs={'class':'form-control','placeholder':'Blog Snippet'}),
      }


class CategoryForm(forms.ModelForm):
   class Meta:
      model = Category
      fields = ('name',)
      
      widgets = {
         'name': forms.TextInput(attrs={'class':'form-control'}),
      }


class CommentForm(forms.ModelForm):
   class Meta:
      model = Comment
      fields = ('name', 'body')
      
      widgets = {
         'name': forms.TextInput(attrs={'class':'form-control'}),
         'body': forms.Textarea(attrs={'class':'form-control'}),
      }


class EditForm(forms.ModelForm):
   class Meta:
      model = Post
      fields = ('title', 'title_tag', 'body', 'snippet','header_image')
      
      widgets = {
         'title': forms.TextInput(attrs={'class':'form-control'}),
         'title_tag': forms.TextInput(attrs={'class':'form-control'}),
         'body': forms.Textarea(attrs={'class':'form-control'}),
         'snippet': forms.Textarea(attrs={'class':'form-control'}),
      }