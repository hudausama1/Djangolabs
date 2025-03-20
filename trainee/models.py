from django.db import models
from course.models import Course
from django.shortcuts import redirect
import os

class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    image = models.ImageField(upload_to='trainee/images')
    createdate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)
    isactive = models.BooleanField(default=True)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Delete old image if a new one is uploaded
        if self.pk:
            try:
                old_trainee = Trainee.objects.get(pk=self.pk)
                if old_trainee.image and old_trainee.image != self.image:
                    old_trainee.image.delete(save=False)
            except Trainee.DoesNotExist:
                pass

        super().save(*args, **kwargs)

    @classmethod
    def addtrainee(cls, name, email, image, courseid):
        try:
            course = Course.getcoursebyid(courseid)
            trainee, created = cls.objects.get_or_create(
                name=name,
                email=email,
                image=image,
                course=course,
                defaults={'isactive': True}
            )
            if not created:
                raise ValueError("Trainee with the same details already exists.")
            return cls.gotoalltrainee()
        except Exception as e:
            raise ValueError(f"Error adding trainee: {str(e)}")

    @classmethod
    def updatetrainee(cls, traineeid, name, email, myimage, courseid):
        try:
            trainee = cls.objects.get(id=traineeid)
            course = Course.getcoursebyid(courseid)
            trainee.name = name
            trainee.email = email
            trainee.image = myimage
            trainee.course = course
            trainee.save()
        except cls.DoesNotExist:
            raise ValueError(f"Trainee with ID {traineeid} does not exist.")
        except Exception as e:
            raise ValueError(f"Error updating trainee: {str(e)}")

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