from django.db import models
from account.models import CustomUser

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=255)
    max_participants = models.IntegerField()

    
    def __str__(self):
        return self.name
    
class EventJudges(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    judge = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.event} - {self.judge}"


class Participant(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    events_registered = models.ManyToManyField(Event, related_name='participants', blank=True)
    
    def __str__(self):
        return self.user.username

class Judge(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    assigned_events = models.ManyToManyField(Event, related_name='judges')
    
    def __str__(self):
        return self.user.username

class Score(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    judge = models.ForeignKey(Judge, on_delete=models.CASCADE)
    score = models.FloatField()
    remarks = models.TextField()
    
    def __str__(self):
        return f"{self.event} - {self.participant} - {self.judge}"

class Certificate(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    certificate_file = models.FileField(upload_to='certificates/')
    
    def __str__(self):
        return f"{self.participant} - {self.event}"

