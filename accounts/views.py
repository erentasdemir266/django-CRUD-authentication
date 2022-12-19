from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def Login_View(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user=authenticate(username=username,password=password)
        login(request,user)
        return redirect('index')
    return render(request,'accounts/form.html',{'form':form,'title':'Giriş Yap'})

def Register_View(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        password=form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user=authenticate(username=user.username,password=password)
        login(request,new_user)
        return redirect('index')
    return render(request,'accounts/form.html',{'form':form,'title':'Kayıt Ol'})



def Logout_View(request):
    logout(request)
    return redirect('index')

