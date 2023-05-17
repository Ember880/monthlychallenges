from django.urls import path
from . import  views


urlpatterns = [
    path("<int:month>", views.monthbynumber),
    path("<str:month>", views.monthly)
]
 
  