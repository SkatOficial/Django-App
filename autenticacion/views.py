from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
# Create your views here.


def registrer(request): 
    if request.method == 'POST':
        try:
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])

                user.save()
                login(request,user)
                return redirect('home')
            else:
                context = {'form': UserCreationForm,
                           'error': "LAS CONTRASEÑAS NO COINCIDEN"}
                return render(request, 'register.html', context)
        except IntegrityError:
            context = {'form': UserCreationForm,
                       'error': "EL USUARIO YA EXISTE"}
            return render(request, 'register.html', context)

    context = {'form': UserCreationForm}
    return render(request, 'register.html', context)

@login_required(login_url='signin')
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if(request.method == 'POST'):
        v_username = request.POST['username']
        v_password = request.POST['password'] 
        user = authenticate(request,username=v_username,password = v_password )
        if user is None:
            context = {'form' : AuthenticationForm,
                       'error': 'USUARIO O CONTRASEÑA INCORRECTOS'}
            return render(request, 'login.html', context)
        login(request,user)
        return redirect('home')    
    else:
        context = {'form' : AuthenticationForm}
        return render(request, 'login.html', context)