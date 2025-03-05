from django import forms
from .models import Contact

# class ContactForm(forms.Form): when you want to build a form without models

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['user_id', 'email', 'message', 'list', 'date'] # These fields show me spesific fields in the form 
        widgets = {
            'user_id': forms.TextInput(attrs={'placeholder': '@jhondoe'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Contact Email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Text', 'rows': 6})
        }