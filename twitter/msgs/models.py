from django.db import models
from users.models import User

class Msg(models.Model):
    sender = models.ForeignKey(User)
    reciever = models.ForeignKey(User)
    content = models.TextField()
    is_read = models.BooleanField()


# Create your models here.
