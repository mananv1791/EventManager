from django.db import models


class ParticipantReg(models.Model):
    CHOICES = [
    ('Online', 'Online'),
    ('Offline', 'Offline')
]
    EventNumber = models.IntegerField(primary_key=True)
    EventName = models.CharField(max_length=300)
    Description = models.CharField(max_length=500)
    Location = models.CharField(max_length=7, choices=CHOICES,default='Online')
    RegFrom = models.DateTimeField()
    RegTo = models.DateTimeField()
    Deadline = models.DateTimeField()
    Email = models.EmailField()
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.EventName


#class EventReg(models.Model):
