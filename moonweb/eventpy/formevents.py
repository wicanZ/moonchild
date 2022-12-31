from django.forms import ModelForm
from django import forms
from moonch3api.models import Event

class EventForm( ModelForm ) :
    date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))
    # time = forms.DateField(
    #     required=True,
    #     widget=forms.TimeInput(attrs={'class': 'form-control', 'type':'time' ,'placeholder': 'Time'}),
    #     input_formats=(
    #         '%h:%m:%s',  # '2006-10-25'
    #         # '%m/%d/%Y',  # '10/25/2006'
    #         # '%m/%d/%y'
    #     )
    #     )
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['user','created','image','time','likes']