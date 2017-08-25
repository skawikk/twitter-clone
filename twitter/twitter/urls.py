"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import users.views
import msgs.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/login/$', users.views.UsersUserLoginView.as_view(), name="users-user-login"),
    url(r'^users/singup/$', users.views.UsersUserSingupView.as_view(), name="users-user-singup"),
    url(r'^users/modify/(?P<pk>\d+)/$', users.views.UsersUserModifyView.as_view(), name="users-user-modify"),
    url(r'^msgs/show/(?P<id>(\d)+)/', msgs.views.ShowView.as_view(), name = 'msgs-show'),
    url(r'^msgs/send_message/(?P<id>(\d)+)/', msgs.views.SendMessageView.as_view(), name='msgs-send-message'),
    url(r'^msgs/show_message/(?P<id>(\d)+)/', msgs.views.ShowMessageView.as_view(), name='msgs-show-message')
]
