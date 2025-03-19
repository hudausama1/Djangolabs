from django.shortcuts import render,redirect
from .models import Trainee
from django.http import HttpResponseRedirect
# Create your views here.
def getalltrainees(req):
    context={}
    #select * from trianee_trainees
    # context['trainees']=Trainee.objects.all()
    context['trainees']=Trainee.objects.filter(isactive=True)
    return render(req,'trainee/list.html',context)
def addtrainees(req):
    if(req.method=='POST'):
        # #get info
        # trname=req.POST['trname']
        # tremail=req.POST['tremail']
        # trimg=req.FILES['trimg']
        # #save db
        # obj=Trainee(name=trname,email=tremail,image=trimg)
        # obj.save()
        Trainee.objects.create(name=req.POST['trname']
                               ,email=req.POST['tremail']
                               ,image=req.FILES['trimg']
                               )
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
