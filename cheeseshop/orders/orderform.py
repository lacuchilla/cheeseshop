from django.utils.translation import gettext_lazy as _
from django import forms

class ContactForm(forms.Form):
    
    name = forms.CharField(label=_("Your Name"),
                           max_length=255,
                           widget=forms.TextInput,
                           )
                           
    email = forms.EmailField(label=_("Email address"))