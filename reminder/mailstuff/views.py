from reminder.constants import EMAIL_HOST_USER

def create_post(**message):
    author = User.objects.get(email=message['from'])
    title = message['subject']
    content = message['plain']

    p = Post.objects.create(
        author = author,
        title = title, 
        content = content,
    )

    send_mail (
        subject='New post created',
        message = content,
        from_email = EMAIL_HOST_USER,
        recipient_list=[message['from']],
        fail_silently=True
    )
        
                              
