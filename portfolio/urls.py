from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),    #this are Html that will be displayed for users to see and have access to...
]
