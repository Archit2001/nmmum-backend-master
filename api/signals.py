from datetime import timedelta
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Blog, Event, FirebaseToken, Notifications


@receiver(pre_save, sender=Blog)
def manipulate_published_at(sender, instance, **kwargs):

    if instance.id is None:
        if instance.published:
            instance.published_at = timezone.now()

    else:
        previous = Blog.objects.get(pk=instance.id)
        if not previous.published and instance.published:
            instance.published_at = timezone.now()


@receiver(post_save, sender=Event)
def set_automatic_notification(sender, instance, **kwargs):
    conditions = [
        {
            'title': 'New Event', 
            'description': instance.description, 
            'trigger_at': timezone.now() + timedelta(minutes=1)
        },
        {
            'title': 'Scheduled Event', 
            'description': f'5 Minutes Remaining.\n{instance.description}', 
            'trigger_at': instance.date - timedelta(minutes=5)
        },
        {
            'title': 'Scheduled Event', 
            'description': f'30 Minutes Remaining.\n{instance.description}', 
            'trigger_at': instance.date - timedelta(minutes=30)
        }
    ]

    for condition in conditions:

        notification = Notifications.objects.create(
            title=condition['title'],
            description=condition['description'],
            trigger_at=condition['trigger_at']
        )

        notification.save()

