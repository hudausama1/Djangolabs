from django.urls import path
from .views import *

urlpatterns=[
    path('',Listview,name='Course'),
    path('Add',Addview,name='Coursenew'),
    path('Update/<int:id>',Updateview, name='Courseupdate'),
    path('Delete/<int:id>', Deleteview, name='Coursedelete'),
    path('<str:name>', Findview, name='Coursefind')
]
