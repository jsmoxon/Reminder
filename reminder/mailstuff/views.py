from reminder.constants import EMAIL_HOST_USER
from models import MailPost

reply_email = '14af7a6e3133f0079033@cloudmailin.net'

def create_post(**message):
    subject = message['subject']
    body = message['plain']
    MailPost(body=body, email=email).save()
    
    send_mail (
        subject='New post created',
        message = content,
        from_email = 'jsmoxon@gmail.com',
        recipient_list=['jsmoxon@gmail.com'],
        fail_silently=True
    )

                              
