from django.contrib import admin

from mainapp.models import Attendee, Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ("id", "name")

class AttendeeAdmin(admin.ModelAdmin):
    model = Attendee

admin.site.register(Event, EventAdmin)
admin.site.register(Attendee, AttendeeAdmin)
