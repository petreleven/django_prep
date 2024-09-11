from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from mainapp.models import Event, Attendee



def homepage(request: HttpRequest):
    events = Event.objects.all()
    return render(request,template_name="index.html",
                  context={"events":events})
def payment(request):
    return render(request, "payment.html")


def payments(request):
    #The rest of your code
    if request.method == "POST":
        data = {"confirmation_code": request.POST.get("confirmation"),
                "phone_number" : request.POST.get("phone_number")}
        
    #The rest of your code


def all_events_single_organizer(request):
    #FETCH ALL EVENTS BY SINGLE ORGANIZER
    current_user = request.user
    all_events = Event.objects.filter(organizer=current_user)
    return render(request, "singleOrganiserEvents.html", {"all_events": all_events})


def singleEvent(request, id):
    ev = Event.objects.get(id=id)
    att = Attendee.objects.filter(event=ev)
    return render(request, "organiserSingleEvent.html", {"ev": ev, "att":att})
