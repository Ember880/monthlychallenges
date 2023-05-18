from django.urls import path
from . import  views


urlpatterns = [
    path("",views.index),
    path("<int:month>", views.monthbynumber),
    path("<str:month>", views.monthly, name= "monthchallenge")
]
 
  