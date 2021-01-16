from django import forms


class ParticipantReg(forms.Form):
    CHOICES = [
    ('Online', 'Online'),
    ('Offline', 'Offline')
]
    EventName = forms.CharField(max_length=300)
    Description = forms.CharField(max_length=500)
    Location = forms.ChoiceField(choices=[('Online','Online'),('Offline','Offline')])
    RegFrom = forms.DateTimeField()
    RegTo = forms.DateTimeField()
    Deadline = forms.DateTimeField()
    Email = forms.EmailField()
    Password = forms.CharField(max_length=100)


