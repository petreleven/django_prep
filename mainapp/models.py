from django.db import models
from django.contrib.auth.models import AbstractUser



class Organizer(AbstractUser):
    ispaidmember = models.BooleanField(default=False)


class Event(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    organizer = models.ForeignKey(to=Organizer, related_name="events", on_delete=models.CASCADE)
    description = models.TextField()
    attendance_date = models.DateTimeField(auto_now_add=True)
    created = models.DateField(auto_now_add=True)
    


class Attendee(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    company_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    #what event
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default="")
    email_has_been_forwarded = models.BooleanField(default=False)
    x = models.BooleanField(default=False)


class DailyEmailsLimit(models.Model):
    sentemails = models.PositiveIntegerField(default=0)
    lastSent = models.DateTimeField()
