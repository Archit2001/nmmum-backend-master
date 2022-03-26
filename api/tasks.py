from logging import error
from django.conf import settings
from backend.celery import app
from django.utils import timezone
from .models import Notifications, FirebaseToken
import requests


NMMUN_ICON_PATH = ''

@app.task
def send_notifications(bind=True):
    tokens = FirebaseToken.objects.all()
    # tokens = [
    #     'd0xwVVubCIDN00Ik-iWp8t:APA91bEwrkh6yJ5hxZZAURo92WFrhJGdyKwG3aynjl_cAuAX286yQGRdHlJCahP3o47xIaxR0vS05VJhxoy6NfrKYRifmODzZNBBwmI96FNysrcbWcrByLUQKxnHqAOOy6nym-LiS7nT',
    #     'cscwoLZwJFBMa-oD0QfBZ1:APA91bFb6qiQqs_5oc0Zj7SnkrO0s8n0wlbP2sx14m5MRKRKOjTcdxyfIWfi8r0JcIym_hy1QMVxNgwhfgwoqLZ7HCytlPqWHpHz6pR7y3f0cq2XTX7p1KDNHym5QvJYLRlVDGNjTFQf'
    # ]

    notifications = Notifications.objects.filter(trigger_at__lt=timezone.now(), triggered=False)
    
    if len(notifications) > 0:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'key={settings.FIREBASE_SERVER_KEY}'
        }

        for notification in notifications:
            payload = {
                'registration_ids': tokens,
                'priority': 'high',
                'notification': {
                    'title': notification.title,
                    'body': notification.description,
                    'icon': NMMUN_ICON_PATH
                }
            }

            try:
                result = requests.post(settings.FIREBASE_SERVER_URL, json=payload, headers=headers)
                
                # Setting trigerred value to be true if the reuqest is completed
                t = Notifications.objects.get(id=notification.id)
                t.triggered = True
                t.save(['triggered'])

            except error:
                print(error)


@app.task()
def checker():
    print("celery checked")