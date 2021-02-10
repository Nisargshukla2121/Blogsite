from django.shortcuts import render, HttpResponse
from blog.models import Post
from django.utils import timezone
from django.conf import settings 
from django.core.mail import send_mail 
from django.conf import settings 
from django.core.mail import send_mail 





def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', context)

def blogMy(request):
    alluserPosts = Post.objects.filter(author = request.user)
    context2 = {'alluserPosts': alluserPosts}
    return render(request, 'blog/blogMy.html', context2)


def blogWrite(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        author = request.user
        post = Post(title=title,content=content,slug=title,author=author)
        
        post.save()  
    return render(request, 'blog/blogWrite.html')

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request, 'blog/blogPost.html', context)
