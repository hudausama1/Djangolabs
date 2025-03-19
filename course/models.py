from django.db import models


# Create your models here.
class Course(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'ID:' + str(self.id) + ' ,Name:' + self.name

    @classmethod
    def getallcourses(cls):
        return cls.objects.all()

    @classmethod
    def getcoursebyid(cls, id):
        return cls.objects.get(id=id)