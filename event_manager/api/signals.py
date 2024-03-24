from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Participant, Event

@receiver(post_save, sender=Participant)
def update_participant_count(sender, instance, created, **kwargs):
    if created:
        event = instance.event
        event.participant_count += 1
        event.save()
        