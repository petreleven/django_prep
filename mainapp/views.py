from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from mainapp.models import Event



def homepage(request: HttpRequest):
    events = Event.objects.all()
    return render(request,template_name="index.html",
                  context={"events":events})
