from django.urls import path
from .views import *
urlpatterns=[
    #path('',getalltrainees,name='trall'),
    path('',TraineeList.as_view(),name='trall'),
    path('Show/<int:pk>', TraineeShow.as_view(), name='trshow'),
    path('Add',TraineeViewAdd_G.as_view,name='tradd'),
    #path('<int:pk>/delete/', TraineeDeleteView.as_view(), name='trdelete'),
    #path('Update/<int:id>',updatetrainees,name='trupdate'),
    path('Delete/<int:pk>/', TraineeDeleteView.as_view(), name='trdelete'),
    #path('Show/<pk>',TraineeShow.as_view(),name='trshow'),
    path('Update/<int:pk>/', TraineeUpdateView.as_view(), name='trupdate'),

]