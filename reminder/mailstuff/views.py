from reminder.constants import EMAIL_HOST_USER
from models import MailPost

reply_email = '14af7a6e3133f0079033@cloudmailin.net'

def create_post(**message):
    title = message['subject']
    content = message['plain']
    p = MailPost.objects.create(
        body = title+content, 
        email = "jsmoxon@gmail.com",
    )
    p.save()
    
    send_mail (
        subject='New post created',
        message = content,
        from_email = reply_email,
        recipient_list=['jsmoxon@gmail.com'],
        fail_silently=True
    )

                              
