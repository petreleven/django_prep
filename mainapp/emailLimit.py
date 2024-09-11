from django.utils import timezone
from datetime import timedelta
from django.db.models import Model

def check_limit(DailyEmailsSent : Model):
  now = timezone.now()
  last_sent = DailyEmailsSent.objects.get_or_create(id = 1).lastSent
  if (now-last_sent) > timedelta(hours=24):
    
