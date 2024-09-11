from django.contrib import admin
from django.contrib.admin import ModelAdmin

from mainapp.models import Attendee, Event, Organizer


class CustomUserAdmin(ModelAdmin):
    model = Organizer

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ("id", "name")

class AttendeeAdmin(admin.ModelAdmin):
    model = Attendee

admin.site.register(Event, EventAdmin)
admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(Organizer, CustomUserAdmin)
