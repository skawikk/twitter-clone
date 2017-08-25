from django.contrib import admin
from users.models import User
from msgs.models import Msg

admin.site.register(User)
admin.site.register(Msg)

# Register your models here.
