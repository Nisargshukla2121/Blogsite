from django.shortcuts import render, HttpResponse
from blog.models import Post
from django.utils import timezone
from django.conf import settings 
from django.core.mail import send_mail 
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.conf import settings 
from django.core.mail import send_mail 


def blogHome(request):
    allPosts = Post.objects.all().order_by('-date_posted')
    allPosts = allPosts.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(allPosts, 3)
    try:
        allPosts = paginator.page(page)
    except PageNotAnInteger:
        allPosts = paginator.page(1)
    except EmptyPage:
        allPosts = paginator.page(paginator.num_pages)
    

    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', context)
    #return render(request, 'blog/blogHome.html', { 'allPosts': allPosts })
@login_required 
def blogMy(request):
    alluserPosts = Post.objects.filter(author = request.user)
   
    page = request.GET.get('page', 1)

    paginator = Paginator(alluserPosts, 3)
    try:
        alluserPosts = paginator.page(page)
    except PageNotAnInteger:
        alluserPosts = paginator.page(1)
    except EmptyPage:
        alluserPosts = paginator.page(paginator.num_pages)
    context2 = {'alluserPosts': alluserPosts}
 
    #return render(request, 'blog/blogHome.html', context2)
    return render(request, 'blog/blogMy.html', context2)

def blogMyDelete(request,sno):
    post = Post.objects.get(sno=sno)
    post.delete()
    return HttpResponse("deleted")

def blogMyEdit(request,sno):
    post = Post.objects.get(sno=sno)
    return render(request,'blog/blogMyEdit.html', {'post':post})

def editcode(request,sno):
    if request.method == "POST":
        title = request.POST['title']
        sno = request.POST['sno']
        content = request.POST['content']
        author = request.user
        contect3 = post.objects.get(sno=sno)
        post = Post(title=title,content=content,slug=sno,author=author)
        post.save()
        return render(request, 'blog/blogWrite.html')  

@login_required
def blogWrite(request,sno):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        author = request.user
        post = Post(title=title,content=content,slug=sno,author=author)
        
        post.save()  

        subject = 'your post added successfyly'
        message = f'Hi {post.author}, Thank you for posting blogs in Blogsite and hoping for some new blog from .you'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [author.email, ]
        send_mail( subject, message, email_from, recipient_list ) 
    return render(request, 'blog/blogWrite.html')

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request, 'blog/blogPost.html', context)


