from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        exclude = ['user', 'article']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'id': 'message',
            'cols': 30,
            'rows': 10,
        })