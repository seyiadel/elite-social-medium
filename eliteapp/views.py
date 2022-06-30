from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import Feedpost, UserProfile
# Create your views here.
def signup(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('.')
            elif User.objects.filter(username=username).exists():
                messages.info(request, " Username is taken, Think of another")
                return redirect('.')
            else:
                user=User.objects.create_user(username=username, email=email, password=password)
                user.save() 

                user_login = authenticate(username=username, password=password)
                login(request, user_login)


                #Create Profile for New User
                user_model=User.objects.get(username=username)
                new_profile=UserProfile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('login') 
        else:
            messages.error(request, 'Password does not match')
            return redirect('signup')

    else:    
        return render(request, "sign-up.html" )


def loggedin(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "You don't have an account.Please sign up")
            return redirect('.')
    return render(request, 'login.html')

@login_required(login_url='login')
def home(request):
    user_objects = User.objects.get(username=request.user.username)
    user_profile = UserProfile.objects.get(user=user_objects)
    feeds = Feedpost.objects.all()
    return render(request, 'home.html',{'user_profile':user_profile, 'feeds':feeds})

@login_required(login_url='login')
def loggedout(request):
    logout(request)
    messages.success(request,'Logged Out Succesfully')
    return redirect('login')

@login_required(login_url='login')
def add_post(request):
    if request.method == 'POST':
        user=request.user.username
        caption=request.POST['caption']
        postimage=request.FILES.get('postimage')
    
        new_post=Feedpost.objects.create(user=user,caption=caption, postimage=postimage)
        new_post.save()
        return redirect('home')
    else:
        return redirect('home')
