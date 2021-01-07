
from django.db import models


class ParticipantReg(models.Model):
    CHOICES = [
    ('Online', 'On'),
    ('Offline', 'Of')
]
    EventName = models.CharField(max_length=300,unique=True)
    Description = models.CharField(max_length=500)
    Location = models.CharField(max_length=7, choices=CHOICES,default='Online')
    RegFrom = models.TimeField()
    RegTo = models.TimeField()
    Deadline = models.TimeField()
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
