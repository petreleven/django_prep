from django.urls import path
from .views import homepage, singleEvent, all_events_single_organizer

urlpatterns = [
    path("", homepage, name="homepage"),
    #rest of your paths
    #........................

    path("organizer_events/", all_events_single_organizer, name="organizer_events"),
    path("singleEvent/<int:id>", singleEvent, name="singleEvent"),
]
