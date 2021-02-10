from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Post
from django.conf import settings 
from django.core.mail import send_mail 




# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "please fill the form correctly")
        else:
            contact = Contact(name=name,email=email,phone=phone, content=content)
            contact.save()
            messages.success(request,"Your message has been successfully sent")

    return render(request, 'home/contact.html')

def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = Post.object.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    if allPosts.count == 0:
            messages.warning(request, "No search result found. please refine your query")
    params = {'allPosts': allPosts, 'query':query}
    return render(request, 'home/search.html',params)

def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
   #     pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username,email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "your Blogsite accound has been successfully created")
        
        
        subject = 'welcome to Blogsite'
        message = f'Hi {myuser.username}, Thank you for registering in Blogsite.'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [myuser.email, ]
        send_mail( subject, message, email_from, recipient_list ) 

        return redirect('home')
    else:
        return HttpResponse('404 - Not found')

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request,"successfully logged in")
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials, please try again")
            return redirect('home')

    return HttpResponse('404- Not Found')

def handleLogout(request):
        logout(request)
        messages.success(request,"successfully logout")
        return redirect('home')