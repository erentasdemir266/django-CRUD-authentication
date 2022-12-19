from django.urls import path
from . import views


app_name='accounts'

urlpatterns = [
    path('login', views.Login_View,name='login'),
    path('register', views.Register_View,name='register'),
    path('logout', views.Logout_View,name='logout'),


]