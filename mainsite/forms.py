from django import forms
from .models import *

class Contact(forms.ModelForm):
     model = ContactForm
     class Meta():
          exclude = ['review', 'status']
          labels = {
               'user_name': 'Your Name',
               'email': 'Your Email',
               'body': 'Message',
          }
