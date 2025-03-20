from django.urls import path
from .views import *
urlpatterns=[
    path('',getalltrainees,name='trall'),
    path('Add',addtrainees,name='tradd'),
    path('Update/<int:id>',updatetrainees,name='trupdate'),
    path('Delete/<int:id>',deletetrainees,name='trdelete'),
    path('Show/<pk>',TraineeShow.as_view(),name='trshow'),

]