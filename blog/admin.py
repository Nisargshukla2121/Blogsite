from django.contrib import admin
from blog.models import Post, BlogComment


admin.site.register(Post)

admin.site.register( BlogComment )



# class PostAdmin(admin.ModelAdmin):
#     list_display = ['Post.author',]
