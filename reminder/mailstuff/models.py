from django.db import models

class MailPost(models.Model):
    """
    test model for storing mail coming in
    """

    body = models.CharField(max_length=5000,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
