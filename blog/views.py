from django.shortcuts import render , HttpResponseRedirect 

from .forms import SignUpForm  , Login , postForm

from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from .models import post

from django.contrib.auth.models import Group
    # User is authenticated
# Create your views here.

def home(request):
    Posts = post.objects.all()
    return render(request, "blog/home.html",{"posts":Posts})
    
def about(request):
    return render(request, "blog/about.html")
    
def contact(request):
    return render(request, "blog/contact.html")

def dashbord(request):
    if request.user.is_authenticated:
        posts = post.objects.all()
        user = request.user 
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request,"blog/dashbord.html",{"posts":posts,"fname":full_name,"groups":gps})
    else:
        return HttpResponseRedirect("/user_login/")
        
    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")
    

def user_signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations you have become a author ...!')
            user = form.save()
           
            group = Group.objects.get(name="Author")
            user.groups.add(group)
            # form = SignUpForm()
    else:   
         form = SignUpForm()

    return render(request,"blog/signup.html",{"form":form})

def user_login(request):
    if not  request.user.is_authenticated:
        if request.method == "POST":
            form = Login(request=request , data = request.POST)
            # form = Login(request.POST)
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request,"You login have successfully....!!!!")
                    return HttpResponseRedirect("/dashbord/")           
        else:
            form = Login()
        return render(request,"blog/login.html",{"form":form})
    else:
        return HttpResponseRedirect("/dashbord/")
        
    
def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = postForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data["title"]
                desc = form.cleaned_data["desc"]
                pst = post(title=title,desc=desc)
                pst.save()

                # form = postForm()
        else:
            form = postForm()
        return render(request,"blog/addpost.html",{'form':form})
    else:
        return HttpResponseRedirect("/login/")
        
        
    
def update_post(request , id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = post.objects.get(pk=id)
            form = postForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = post.objects.get(pk=id)
            form = postForm(instance=pi)
        return render(request,"blog/updatepost.html",{"form":form})
    else:
        return HttpResponseRedirect("/login/")

        
    
def delete_post(request , id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = post.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect("/dashbord/")
    else:
        return HttpResponseRedirect("/login/")
