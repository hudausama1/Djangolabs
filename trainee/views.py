from django.shortcuts import render,redirect
from .models import Trainee
from course.models import Course

from django.http import HttpResponseRedirect,HttpResponse

from ..course.models import Course


# Create your views here.
def getalltrainees(req):
    context={}
    #select * from trianee_trainees
    # context['trainees']=Trainee.objects.all()
    context['trainees']=Trainee.objects.filter(isactive=True)
    return render(req,'trainee/list.html',context)
def addtrainees(req):
    context={'course':Course.getallcourses()}
    if(req.method=='POST'):
        Trainee.addtrainee(req.POST['trname']
                               ,req.POST['tremail']
                               ,req.FILES['trimg']
                               ,req.POST["trcourse"])
        return redirect('trall')
    return render(req,'trainee/add.html')
def updatetrainees(req,id):
    context={'oldobj':
             Trainee.objects.get(id=id)}
    if(req.method=='POST'):
        Trainee.objects.filter(id=id).update(
            name=req.POST['trname'],
            email=req.POST['tremail'],
            image=req.FILES['trimg'],
        )
        return  redirect('trall')
    return render(req, 'trainee/update.html',context)
def deletetrainees(req,id):
    #hard delete
    # Trainee.objects.filter(id=id).delete()
    #soft deleet
    Trainee.objects.filter(id=id).update(isactive=False)
    # return HttpResponseRedirect('/Trainee/')
    return  redirect('trall')
