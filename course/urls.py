from django.urls import path
from .views import *
from .api.views import update_course
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api.views import CourseViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)  # Register the CourseViewSet

urlpatterns = [
    path('', Listview, name='Course'),
    path('Add', Addview, name='Coursenew'),
    path('Update/<int:id>', Updateview, name='Courseupdate'),
    path('Delete/<int:id>', Deleteview, name='Coursedelete'),
    path('<str:name>', Findview, name='Coursefind'),  # Add a comma here
    path('api/courses/update/<int:pk>/', update_course, name='course-update'),
    path('api/', include(router.urls)),  # Include the router's URLs

]