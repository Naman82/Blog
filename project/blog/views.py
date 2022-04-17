from django.shortcuts import render
from blog.models import Post
# Create your views here.

def home(request):
    return render(request,'home.html')

def profile(request):
    return render(request,'profile.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def addpost(request):
    return render(request, 'Addpost.html')

def post(request):
    if request.method == 'POST':
        image=request.FILES['posts']
        content=request.POST['content']

    post=Post(content=content , image=image)
    post.save()
    return render(request, 'home.html')