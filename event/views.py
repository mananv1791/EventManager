import os,datetime,requests,json
from django.shortcuts import render,redirect
import requests,templates
from django.http import HttpResponse
from .models import EventReg,ParticipantReg
from django.db import IntegrityError
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from datetime import date
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from twilio.rest import Client


def Homepage(request):
    return render(request,"Base.html")



def EventRegistrationView(request):
    try:
        if request.method=='POST':
            random = request.POST
            GDict = {}

            for x,y in random.items():
                if x!='csrfmiddlewaretoken':
                    GDict.update({x:y})
            print(f'\n{GDict}')
            HostEmail = request.POST.get("Email")

            subject='Notification Check {Event Manager}'
            message=f'Hi {HostEmail},\nthank you for Registration,\nHostEmail : {HostEmail} \n Contact Us at {settings.EMAIL_HOST_USER} for any queries '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [HostEmail]
            send_mail(subject,message,email_from,recipient_list)

            EventReg.objects.create(**GDict)
            return render(request,'Main/EventRegistration.html')
        else:
            return render(request,'Main/EventRegistration.html')

    except IntegrityError as e:
        return render(request,"Main/IntegrityError.html")

    
    


def ParticipantRegistration(request):
    context = {
        "EventName":EventReg.objects.filter(RegFrom__gte=date.today())
    }


    try:
        if request.method=='POST':
            random = request.POST
            HDict = {}

            for x,y in random.items():
                if x!='csrfmiddlewaretoken':
                    HDict.update({x:y})
            toEmail = request.POST.get('Email')
            number = request.POST.get('ContactNumber')
            ParName = request.POST.get('ParticipantName')
            EventNam = request.POST.get('Event')
            
            print(number)
            if validate_email(toEmail):
                raise ValidationError("Email is not valid")
                
            else:
                ParticipantReg.objects.create(**HDict)
                print(HDict)
                fromEmail = 'mananv1791@gmail.com'
                toEmail = HDict['Email']
                Subject = 'Bot Message'
                Message = f'Hey {ParName}, \n You have registerd in our event \n Thanks for taking part. \n Have a good day!'
                send_mail(Subject,Message,fromEmail,[toEmail],fail_silently=False)
            
            client = Client("", "")
            client.messages.create(from_="",body=Message,to='+91'+str(number))
            

            return render(request,"Main/ParticipantRegistration.html",context)
        else:
            return render(request,"Main/ParticipantRegistration.html",context)
    except IntegrityError as e:
        return render(request,"Main/Integrity.html")
    except ValidationError as e:
        return render(request,"Main/EmailaddError.html")

def EventDashboard(request):

    data = EventReg.objects.all()

    context = {
        "EventsNameasdf":EventReg.objects.all()
    }
    print(data)
    return render(request, "Main/EventDashboard.html",context)


def Message(request, PhoneNumber):

    
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

    return HttpResponse(returnMessage + response.text)


def EMail(request):
    return HttpResponse("E-mail API")


def TwilioMessage(request,Nuber):
    # /usr/bin/env python
    # Download the twilio-python library from twilio.com/docs/libraries/python


    # Find these values at https://twilio.com/user/account
    # To set up environmental variables, see http://twil.io/secure
    account_sid = os.environ['']
    auth_token = os.environ['']

    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        to=Number,
        from_="",
        body="Hello there this is bot msg")

def integrity(request):
    return render(request,"Main/IntegrityError.html")