from .models import Booking,UserComments
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model= UserComments
        fields= '__all__'
