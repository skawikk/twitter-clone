from django.db import models
from users.models import User

class Msg(models.Model):
    sender = models.ForeignKey(User, related_name='sender')
    reciever = models.ForeignKey(User, related_name='reciever')
    content = models.TextField()
    is_read = models.BooleanField()


# Create your models here.
