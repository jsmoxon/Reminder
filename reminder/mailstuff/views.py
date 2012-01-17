from reminder.constants import EMAIL_HOST_USER

reply_email = '14af7a6e3133f0079033@cloudmailin.net'

def create_post(**message):
    author = User.objects.get(email=message['from'])
    print author
    title = message['subject']
    content = message['plain']

    p = Post.objects.create(
        author = author,
        title = title, 
        content = content,
    )
    print p
    send_mail (
        subject='New post created',
        message = content,
        from_email = reply_email,
        recipient_list=['jsmoxon@gmail.com']
        fail_silently=True
    )
    print p, author, subject
                              
