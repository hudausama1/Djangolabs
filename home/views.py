from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def Loginview(req):
    return HttpResponse('<h1>hi login</h1>')

def Logoutview(req):
    return HttpResponse('<h1>hi logout</h1>')

def Regview(req):
    return HttpResponse('<h1>hi Reg</h1>')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

