from django import forms
from .models import Contact


class ContactForms(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            "class": 'form-control',
            "placeholder": 'Your name'
        })
        self.fields['email'].widget.attrs.update({
            "class": 'form-control',
            "placeholder": 'Email'
        })
        self.fields['subject'].widget.attrs.update({
            "class": 'form-control',
            "placeholder": 'Subject'
        })
        self.fields['message'].widget.attrs.update({
            "class": 'form-control',
            "placeholder": 'Message'
        })