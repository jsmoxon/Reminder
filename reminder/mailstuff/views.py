from reminder.constants import EMAIL_HOST_USER

reply_email = '14af7a6e3133f0079033@cloudmailin.net'

def create_post(**message):
    title = message['subject']
    content = message['plain']
    p = MailPost.objects.create(
        author = author,
        title = title, 
        content = content,
    )
    p.save()
    
    send_mail (
        subject='New post created',
        message = content,
        from_email = reply_email,
        recipient_list=['jsmoxon@gmail.com'],
        fail_silently=True
    )

                              
