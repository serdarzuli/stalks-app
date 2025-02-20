from django import forms
from .models import Contact

# class ContactForm(forms.Form): when you want to build a form without models

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'dept', 'date'] # These fields show me spesific fields in the form 
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'FullName'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Write your text', 'rows': 6})
        }