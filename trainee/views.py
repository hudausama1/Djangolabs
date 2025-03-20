from django.shortcuts import render,redirect
from .models import Trainee
from course.models import Course
from .forms import Traineeadd, Traineeaddmodel

from django.http import HttpResponseRedirect,HttpResponse
from django.views import View
from django.views.generic import CreateView,UpdateView,ListView,DetailView,DeleteView
#from ..course.models import Course

class TraineeShow(DetailView):#id
    model = Trainee
    context_object_name = 'trainee'


# Create your views here.
def getalltrainees(req):
    context={}
    #select * from trianee_trainees
    # context['trainees']=Trainee.objects.all()
    context['trainees']=Trainee.getallactivetrainee()
    return render(req,'trainee/list.html',context)

#@login_required()
def addtrainees(req):
    context = {'course': Course.getallcourses(),
               'form': Traineeaddmodel()}

    if(req.method=='POST' ):
        form=Traineeaddmodel(data=req.POST,files=req.FILES)
        if(form.is_bound and form.is_valid()):
            form.save()
            return Trainee.gotoalltrainee()
        else:
            context['error']=form.errors
            return render(req, 'trainee/addform.html', context)
    return render(req,'trainee/addform.html',context)

def updatetrainees(req,id):
    context={'oldobj':Trainee.gettraineebyid(id=id),'course':Course.getallcourses()}
    if(req.method=='POST'):
        Trainee.updatetrainee(traineeid=id,
            name=req.POST['trname'],
            email=req.POST['tremail'],
            image=req.FILES['trimg'],
            courseid=req.POST['trcourse']
        )
        return  Trainee.gotoalltrainee()
    return render(req, 'trainee/update.html',context)
def deletetrainees(req,id):
    #hard delete
    # Trainee.objects.filter(id=id).delete()
    #soft deleet
    Trainee.objects.filter(id=id).update(isactive=False)
    # return HttpResponseRedirect('/Trainee/')
    return  redirect('trall')
