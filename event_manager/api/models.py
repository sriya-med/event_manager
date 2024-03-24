from django.db import models
from django.contrib.auth.models import User
#from .models import Event


# Create your models here.
class Event(models.Model):
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    event_name = models.CharField(max_length=50)
    event_date = models.DateTimeField()
    event_location = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank=True)
    participant_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Created event: {self.event_name} for {self.event_date} at {self.event_location}"


class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    signup_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} signed up for {self.event.event_name}"

