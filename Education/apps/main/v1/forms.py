from django import forms
from apps.main.models import Contact, Subscribe


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control py-2',
            'type': 'text',
            'id': 'name'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control py-2',
            'type': 'email',
            'id': 'email'
        })
        self.fields['body'].widget.attrs.update({
            'class': 'form-control py-2',
            'cols': 30,
            'type': 'message',
            'id': 'message'
        })


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control email',
            'type': 'email',
            'placeholder': 'Enter email'
        })