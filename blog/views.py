from django.shortcuts import render, HttpResponse,redirect
from blog.models import Post ,BlogComment
from django.utils import timezone
from django.conf import settings 
from django.core.mail import send_mail 
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.conf import settings 
from django.core.mail import send_mail 
from django.contrib import messages

#home page for all blogs
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
    return render(request, '../templates/blog/blogHome.html', context)
    #return render(request, 'blog/blogHome.html', { 'allPosts': allPosts })

#myblog page for logged in user
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
    return render(request, '../templates/blog/blogMy.html', context2)

#blog delete
def blogMyDelete(request,sno):
    post = Post.objects.get(sno=sno)
    post.delete()
    #return render(request, 'blog/blogMy.html')
    return redirect('blogMy')

#blog edit
def blogMyEdit(request,sno):
    post = Post.objects.get(sno=sno)

    if request.method == "POST":
        post = Post.objects.filter(sno=sno)
        title = request.POST['title']
        #sno = request.POST['sno']
        content = request.POST['content']
        author = request.user
        category = request.POST['category']
        post.update(title=title,slug=title,sno=sno,content=content,author=author,category=category)
        return redirect('blogMy')   
    return render(request,'../templates/blog/blogMyEdit.html', {'post':post})

#add blog
@login_required
def blogWrite(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        author = request.user
    
        category = request.POST['category']
        post = Post(title=title,content=content,slug=title,author=author,category=category)
        
        post.save()  

        subject = 'your post added successfly'
        message = f'Hi {post.author}, Thank you for posting blogs in Blogsite and hoping for some new blog from .you'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [author.email, ]
        send_mail( subject, message, email_from, recipient_list ) 
    return render(request, '../templates/blog/blogWrite.html')

#detail view and comments in blog 
def blogPost(request, slug): 
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        comment=BlogComment(comment= comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
        return redirect(f"/blog/{post.slug}")
    
    post=Post.objects.filter(slug=slug).first()
    post.views = post.views + 1 
    post.save()
    print (post.views)
    comments= BlogComment.objects.filter(post=post)
    context={'post':post, 'comments': comments}
    return render(request, "../templates/blog/blogPost.html", context)

