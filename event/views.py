from django.shortcuts import render
import requests,templates
from django.http import HttpResponse
import datetime


def Homepage(request):
    return render(request,"Base.html")


def EventReg(request):
    return render(request, "Main/EventRegistration.html")


def ParticipantReg(request):
    return render(request, "Main/ParticipantRegistration.html")


def EventDashboard(request):
    return render(request, "Main/EventDashboard.html")


def Message(request, PhoneNumber):
    import requests
    defaultNumber = 6352512793
    url = "https://www.fast2sms.com/dev/bulk"
    message = datetime.datetime.now
    querystring = {"authorization":"O5hePUfZv1wY5lc8HF5zq4iA3wYdnl4GbK7mm8mVRInOftNeulbzLFSVXGfW","sender_id":"FSTSMS",
                   "message":"This is test message","language":"english","route":"p","numbers": PhoneNumber}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    returnMessage = response.text

    querystring = {"authorization": "O5hePUfZv1wY5lc8HF5zq4iA3wYdnl4GbK7mm8mVRInOftNeulbzLFSVXGfW",
                   "sender_id": "FSTSMS",
                   "message": "This is test message", "language": "english", "route": "p", "numbers": defaultNumber}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return HttpResponse(returnMessage + response.text)
