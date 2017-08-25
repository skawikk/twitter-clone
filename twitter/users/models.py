from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.urls import reverse


class User(AbstractUser):
    # login = models.CharField(max_length=64, unique=True, primary_key=True)
    # first_name = models.CharField(max_length=64, blank=True, null=True)
    # last_name = models.CharField(max_length=64, blank=True, null=True)
    # date_joined = models.DateTimeField(auto_now_add=True)
    # last_login = models.DateTimeField()
    # password = models.CharField(max_length=64)
    # email = models.EmailField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_modify_url(self):
        return reverse("users-user-modify", kwargs={"pk": self.id})
