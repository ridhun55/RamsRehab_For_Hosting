from django.contrib import admin
from .models import Post, Comment
from .models import Category

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)