from django import forms

class SendMessageForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)