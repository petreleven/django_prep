from django.db import models


class Event(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


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

    
