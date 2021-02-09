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


def blogWrite(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST['author']
        post = Post(title=title,content=content,author=author,slug=title).save()

            
        subject = 'welcome to Blogsite'
        message = f'Hi {myuser.username}, thank you for uploading post in our website.'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [myuser.email, ]
        send_mail( subject, message, email_from, recipient_list ) 
    return render(request, 'blog/blogWrite.html')

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request, 'blog/blogPost.html', context)

    
    
        
        
        
    