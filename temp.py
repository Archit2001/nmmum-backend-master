# COMMAND 1
celery -A backend worker --loglevel=info

# COMMAND 2
celery -A backend beat -l info --scheduler djangoers:DatabaseScheduler --loglevel=info

# from django.utils import timezone
# import requests
# import json

# FIREBASE_SERVER_KEY = 'AAAAjE4mM94:APA91bGCaVDXZjlBMNJknsGkPeBBNZMxhKvmUbsnHnyerXZ2J55qN-iWaybxIq2Fgs58Iw9Wws7J9_wkFnVMPeCUjb8CcZgkLmvWB1r0DQ-6W0F9AZzJeL_217b821jO1jxB-f4tTmGJ'

# def send_notifications():
#     # tokens = FirebaseToken.objects.all()
#     tokens = [
#         'd0xwVVubCIDN00Ik-iWp8t:APA91bEwrkh6yJ5hxZZAURo92WFrhJGdyKwG3aynjl_cAuAX286yQGRdHlJCahP3o47xIaxR0vS05VJhxoy6NfrKYRifmODzZNBBwmI96FNysrcbWcrByLUQKxnHqAOOy6nym-LiS7nT',
#         'cscwoLZwJFBMa-oD0QfBZ1:APA91bFb6qiQqs_5oc0Zj7SnkrO0s8n0wlbP2sx14m5MRKRKOjTcdxyfIWfi8r0JcIym_hy1QMVxNgwhfgwoqLZ7HCytlPqWHpHz6pR7y3f0cq2XTX7p1KDNHym5QvJYLRlVDGNjTFQf'
#     ]
    
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'key={FIREBASE_SERVER_KEY}'
#     }


#     payload = {
#         'registration_ids': tokens,
#         'priority': 'high',
#         'notification': {
#             'title': 'notification.title',
#             'body': 'madarchod'
#         }
#     }

#     result =  requests.post('https://fcm.googleapis.com/fcm/send', json=payload, headers=headers)
#     print(result)

# # send_notifications()

# print(timezone.now())