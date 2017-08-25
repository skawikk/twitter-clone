from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, View, DetailView
from msgs.models import Msg
from users.models import User
from msgs.forms import SendMessageForm

class ShowView(ListView):
    model = Msg

    def get_queryset(self):
        queryset = super().get_queryset()
        user = User.objects.get(id = self.kwargs['id'])
        queryset1 = queryset.filter(reciever=user)
        queryset2 = queryset.filter(sender=user)
        return queryset1 | queryset2

class SendMessageView(View):
    def get(self, request, id):
        form = SendMessageForm()
        return render(request, 'msgs/generic_form.html',\
                      {'form': form})
    def post(self, request, id):
        sender = request.user
        reciever = User.objects.get(id=id)
        if sender == reciever:
            return redirect('/') #cannot send to yourself
        form = SendMessageForm(data=request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            Msg.objects.create(sender=sender, reciever=reciever, content=content, is_read=False)
        return redirect('/')

class ShowMessageView(DetailView):
    model = Msg
    pk_url_kwarg='id'

    def get(self, *args, **kwargs):
        return_value = super().get(*args, **kwargs)
        self.object.is_read = True
        self.object.save()
        return return_value


# Create your views here.
