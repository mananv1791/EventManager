from django.db import models


class ParticipantReg(models.Model):
    
    EventName = models.CharField(max_length=300)
    Description = models.CharField(max_length=500)
    Location = models.CharField(max_length=200)
    RegFrom = models.DateTimeField()
    RegTo = models.DateTimeField()
    Deadline = models.DateTimeField()
    Email = models.EmailField()
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.EventName


#class EventReg(models.Model):
