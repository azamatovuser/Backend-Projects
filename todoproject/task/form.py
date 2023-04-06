from django import forms
from .models import Task


class CreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['user', 'title', 'status', 'priority', 'description', 'deadline']
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['status'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['priority'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'col': '10',
            'row': '3',
        })
        self.fields['deadline'].widget.attrs.update({
            'class': 'form-control'
        })