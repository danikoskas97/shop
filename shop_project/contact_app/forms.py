from django import forms
from contact_app.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['subject','text','email']
        widgets = {
        'subject':forms.TextInput(attrs={
            'id':'contact-subject',
            'placeholder':'subject',
            'required':True
            }),
        'email':forms.EmailInput(attrs={
            'id':'contact-email',
            'placeholder':'email',
            'required':True
            }),
        'text':forms.Textarea(attrs={
            'id':'contact-text',
            'placeholder':'Write a text here ...',
            'required':True
            }),
        }
