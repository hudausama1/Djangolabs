from django.db import models
from course.models import Course
from django.shortcuts import redirect
import os

# Create your models here.
class Trainee(models.Model):
    #id auto,name,image,creatdate,email
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    #image path upload image to it &
    image=models.ImageField(upload_to='trainee/images')
    createdate=models.DateTimeField(auto_now_add=True)
    updateddate=models.DateTimeField(auto_now=True)
    isactive=models.BooleanField(default=True)
    course=models.ForeignKey(to=Course,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Delete old image if a new one is uploaded
        if self.pk:
            old_profile = Trainee.objects.filter(pk=self.pk).first()
            if old_profile and old_profile.image and old_profile.image != self.image:
                old_image_path = os.path.join(old_profile.image.path)
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)
        # not db
        super().save(*args, **kwargs)  # ✅ Ensures correct upload path

    @classmethod
    def addtrainee(cls, name, email, image, courseid):
        Trainee.objects.create(name=name
                               , email=email
                               , image=image
                               , course=Course.getcoursebyid(courseid))
        return Trainee.gotoalltrainee()

    @classmethod
    def updatetrainee(cls, traineeid, name, email, myimage, courseid, traineeobj):
        # print(image,type(image))
        cls.objects.filter(id=traineeid).update(name=name
                                                , email=email
                                                , image=myimage
                                                , course=Course.getcoursebyid(courseid))
    @staticmethod
    def gotoalltrainee():
        return redirect('trall')

    @classmethod
    def getallactivetrainee(cls):
        return cls.objects.filter(isactive=True)

    @classmethod
    def gettraineebyid(cls, id):
        return cls.objects.get(id=id)

    def getimageurl(self):
        return '/media/' + self.image