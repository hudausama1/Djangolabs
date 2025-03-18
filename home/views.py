from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Loginview(req):
    return HttpResponse('<h1>hi login</h1>')

def Logoutview(req):
    return HttpResponse('<h1>hi logout</h1>')

def Regview(req):
    return HttpResponse('<h1>hi Reg</h1>')
