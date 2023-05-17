from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

monthlychallenges = {
    "january":"hello man",
    "february":"yoo whats good",
    "march":"how are you man",
    "april":"dont do that",
    "may":"tell me",
    "june":"go back",
    "july":"enjoy the moment",
    "august":"listen to some music",
    "september":"read more",
    "october":"dress well",
    "november":"eat healthy foods",
    "december":"party timmmmeeee!"    
}


def monthbynumber(request, month):
    return HttpResponse(month)


def monthly(request, month):
    try:
        challenge_rule = monthlychallenges[month]
    except:
        return HttpResponseNotFound("this is man is not available for humans")    


    
    return HttpResponse(challenge_rule)