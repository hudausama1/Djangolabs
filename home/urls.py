from django.urls import path, include
from .views import *
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[
    path('login/', LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]
