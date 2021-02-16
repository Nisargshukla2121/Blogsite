from django.contrib import admin
from blog.models import Post, BlogComment, BlogCategory

admin.site.register((Post, BlogComment, BlogCategory))
