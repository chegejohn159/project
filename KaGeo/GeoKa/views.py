from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import superuser_required

from .forms import form1
from .forms import movie1
from .forms import char1


# def login(request):
#     email = request.POST['email']
#     password = request.POST['password']
#     user = authenticate(request, username=email, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('/')
#         # Redirect to a success page.
#         ...
#     else:
#         # Return an 'invalid login' error message.
#         ...

def index(request):
    return render(request, 'index.html', {'name':"malkie"})


def signup(request):
    if request.method == 'POST':
        form = form1(request.POST)

        # firstname = form.data['firstname']
        # middlename = form.data['middlename']
        # password = form.data['password']
        # password1=form.data['password1']
        # email = form.data['email']


        if form.is_valid():

            user = form.save()
            #user.is_staff=True
            #user.is_superuser=True
            user.set_password(user.password)
            user.save()
            
            #form.save()
            return redirect('/')
    else:
        form = form1()
    return render(request, 'signup.html', {'form': form})

def movie(request):
    if request.method == 'POST':
        form = movie1(request.POST)
        if form.is_valid():
            #writer=user.username

            form.save()

            #form.save()
            return redirect('/')
    else:
        form = movie1()
    return render(request, 'page.html', {'form': form})


def main(request):
    if request.method == 'POST':
        print(request.POST)
        form = char1(request.POST)
        if form.is_valid():

            
            form.save()

            #form.save()
            return redirect('/')
    else:
        form = char1()
    return render(request, 'cat.html', {'form': form})