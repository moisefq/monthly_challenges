from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenge = {
    "january": "this is january",
    "feburary": "this is feburary",
    "march": "this is march",
    "april": "this is april",
    "may": "this is may",
    "june": "this is june",
    "july": "this is july",
    "august": "this is august",
    "september": "this is september",
    "octuber": "this is octuber",
    "november": "this is november",
    "december": "thi is december"
}

# Create your views here.


def monthly_challange_by_numbers(request, month):
    my_value = list(monthly_challenge.keys())

    if month >len(my_value):
        return HttpResponse("this is not the correct month")    

    my_month = my_value[month -1 ]
    redirect_path = reverse("month-challenge", args=[my_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challange(request, month):
    try:
        challenge_text = monthly_challenge[month],
        return HttpResponse(challenge_text)
    except:
        return HttpResponse("the month is supported yet!")