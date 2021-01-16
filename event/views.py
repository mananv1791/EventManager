import os
from django.shortcuts import render,redirect
import requests,templates
from django.http import HttpResponse
import datetime
from .forms import ParticipantReg
from .models import ParticipantReg
from django.db import IntegrityError
from django.core.mail import send_mail
from twilio.rest import Client

def form(request):
    form = ParticipantReg(request.POST or None)
    return render(request,'form.html', {'form':form})


def Homepage(request):
    return render(request,"Base.html")


def EventReg(request):
    try:
        if request.method=='POST':
            random = request.POST
            GDict = {}

            for x,y in random.items():
                if x!='csrfmiddlewaretoken':
                    GDict.update({x:y})
            print(f'\n{GDict}')

            ParticipantReg.objects.create(**GDict)
            send_mail(
                        'Django Test Mail',
                        'This one is msg',
                        'mananv1791@gmail.com',
                        ['mananv17@gmail.com'],
                        fail_silently=False,
                    )
            return render(request,'Main/EventRegistration.html')
        else:
            return render(request,'Main/EventRegistration.html')

    except IntegrityError as e:
        return render(request,"Main/IntegrityError.html")


def ParticipantRegistration(request):

    return render(request,"Main/ParticipantRegistration.html")

def EventDashboard(request):

    ShowData = ParticipantReg.objects.all()

    show = {
        "EventNumber":ShowData
    }

    return render("Main/EventDashboard.html",show)


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


def EMail(request):
    return HttpResponse("E-mail API")


def TwilioMessage(request,Nuber):
    # /usr/bin/env python
    # Download the twilio-python library from twilio.com/docs/libraries/python
    

    # Find these values at https://twilio.com/user/account
    # To set up environmental variables, see http://twil.io/secure
    account_sid = os.environ['ACf2bcb534ef76138e42f6ecfedef6f35d']
    auth_token = os.environ['154b69da2187017628e181bc22427cda']

    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        to=Number,
        from_="6352512793",
        body="Hello there this is bot msg")
