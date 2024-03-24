from django import forms

class EventForm(forms.Form):
    event_name = forms.CharField(max_length=50)
    event_date = forms.DateTimeField()
    event_location = forms.CharField(max_length=50)
    description = forms.CharField(max_length=300, required=False)
    participant_count = forms.IntegerField(initial=0)

class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())