from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# ========= Post ==========================================

class Post(models.Model):
   title = models.CharField(max_length=255)
   header_image = models.ImageField(blank=True, null=True, upload_to="images/")
   title_tag = models.CharField(max_length=255, default="Ram's Rehab")
   author = models.ForeignKey(User,on_delete=models.CASCADE)
   body = RichTextField(blank=True, null=True)
   post_date = models.DateField(auto_now_add=True)
   category = models.CharField(max_length=255,blank=True, null=True, default='others')
   snippet = models.CharField(max_length=255)
   likes = models.ManyToManyField(User, related_name='blog_posts')
   
   def total_likes(self):
      return self.likes.count()
   
   def __str__(self):
      return self.title + ' | ' + str(self.author)

   def get_absolute_url(self):
      return reverse('blog_home')


# ====== Category ======================================

class Category(models.Model):
   name = models.CharField(max_length=255, default='', blank=True, null=True)
   
   def __str__(self):
      return self.name
   
   def get_absolute_url(self):
      return reverse('blog_home')

# ====== Comment ====================================

class Comment(models.Model):
   post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
   name = models.CharField(max_length=255)
   body = models.TextField()
   date_added = models.DateTimeField(auto_now_add=True)
   
   def  __str__(self):
      return '%s - %s' % (self.post.title, self.name)