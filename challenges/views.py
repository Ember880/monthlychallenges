from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
# Create your views here.

monthlychallenges = {
    "january":"hello man",
    "february":"yoo whats good",
    "march":"how are you man",
    "april":"don't do that",
    "may":"tell me",
    "june":"go back",
    "july":"enjoy the moment",
    "august":"listen to some music",
    "september":"read more",
    "october":"dress well",
    "november":"eat healthy foods",
    "december":"party timmmmeeee!"    
}

def index(request):
    list_items = ""
    months = list(monthlychallenges.keys())
    for mon in months:
        capitalized_month = mon.capitalize()
        month_path = reverse("monthchallenge", args=[mon])
        list_items += f"<li><a href =\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<u>{list_items}</u>"
    return HttpResponse(response_data)


def monthbynumber(request, month):
    numbermonth = list(monthlychallenges.keys())
    if month > len(numbermonth):
        return HttpResponseNotFound("how many months are on your calendar?")
    redirect_month = numbermonth[month -1 ]

    redirect_path = reverse("monthchallenge", args=[redirect_month])

    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly(request, month):  
    try:
        challenge_rule = monthlychallenges[month]
        respond_data = f"<h1>{challenge_rule}</h1>"
        return HttpResponse(respond_data) 
    except:
        return HttpResponseNotFound("this month is not available for humans")    


    
     