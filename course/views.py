from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Listview(req):
    courses = [
        [1, 'python'],
        [2, 'php'],
        [3, 'Java'],
    ]
    #return HttpResponse('<h1>courses</h1>')
    return render(req,'course/list.html',context={
        'courses':courses
    })

def Addview(req):
    #return HttpResponse('<h1>add course</h1>')
    return render(req,'course/new.html')


def Updateview(req,id):
    return HttpResponse(f'<h1>update course{id}</h1>')

def Deleteview(req,id):
    return HttpResponse(f'<h1>delete course{id}</h1>')

def Findview(req,name):
    return HttpResponse(f'<h1>find course {name}</h1>')