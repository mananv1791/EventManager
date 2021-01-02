from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [

    path('',views.Homepage),
    path('Base',views.Homepage,name='Homepage'),
    path('ParticipantRegistration/',views.ParticipantReg, name='PR'),
    path('EventRegistration/',views.EventReg, name='ER'),
    path('EventDashboard/',views.EventDashboard, name='ED'),

]
