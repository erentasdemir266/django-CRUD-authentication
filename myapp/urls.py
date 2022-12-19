from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('create', views.create,name='create'),
    path('<slug:slug>', views.detail,name='detail'),
    path('<slug:slug>/update', views.update,name='update'),
    path('<slug:slug>/delete', views.delete,name='delete'),


]