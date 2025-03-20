from curses.textpad import Textbox
from django import forms
from django.forms import TextInput
from course.models import Course
from .models import Trainee
# describe form
class Traineeaddmodel(forms.ModelForm):
    class Meta:
        model=Trainee
        # fields=['name','email']
        fields='__all__'
        exclude=['isactive']

class Traineeadd(forms.Form):
    #input text
    trname=forms.CharField(
        label='Full Name',
        required=True,min_length=3,max_length=10,
    )
    tremail=forms.EmailField(label='Email')
    trimg=forms.ImageField(label='Profile Image')
    #choises tuple of tuples
    # trtrack=forms.ChoiceField(widget=forms.SelectMultiple,
    #     choices=[(track.id,track.name) for track in Track2.getalltracks()]
    # )
    # test=forms.DateTimeField()