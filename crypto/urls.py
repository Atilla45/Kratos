from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('sign-up', views.SignUp.as_view(), name='signup'),
    path('login', views.SignIn.as_view(), name='login'),
    # path('about', views.AboutUs.as_view(), name='about'),
]
