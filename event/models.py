from django.db import models
counter=0

class EventReg(models.Model):
    EventName = models.CharField(max_length=300, default="random")
    Description = models.CharField(max_length=500, default="random")
    Location = models.CharField(max_length=200, default="random")
    RegFrom = models.DateTimeField()
    RegTo = models.DateTimeField()
    Deadline = models.DateTimeField()
    Email = models.EmailField()
    Password = models.CharField(max_length=100, default="random")
    
    def __str__(self):
        return self.EventName



class ParticipantReg(models.Model):
    
    
    ParticipantName = models.CharField(max_length=300, default="random")
    ContactNumber = models.IntegerField( default="0000000000")
    Email = models.EmailField()
    Event = models.CharField(max_length=100 ,default='SampleEvent')
    RegistrationType = models.CharField(max_length=50,default="NA")
    NumOfPeople = models.IntegerField(default="1")

    def __str__(self):    
        return self.ParticipantName
