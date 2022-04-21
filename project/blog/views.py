from django.shortcuts import render,redirect
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    posts=Post.objects.all()
    # print(post.image.url)
    return render(request,'home.html',{'posts':posts})

def profile(request):
    return render(request,'profile.html')

def login(request):
    if request.method =='POST':
        email=request.POST['email']
        password=request.POST['password']

        user=auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2 :
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used !')
                return redirect('register')
            else:
                user=User.objects.create_user(username=email,email=email,password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password did not match')
            return redirect('register')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def addpost(request):
    return render(request, 'Addpost.html')

def post(request):
    if request.method == 'POST':
        image=request.FILES['posts']
        content=request.POST['content']
        user= request.user

    post=Post(user=user,content=content,image=image)
    post.save()
    return redirect('/')
    
