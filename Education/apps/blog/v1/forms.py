from django import forms
from apps.blog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs.update({
            'class': 'form-control',
            'type': 'text',
        })
        self.fields['body'].widget.attrs.update({
            'class': 'form-control',
            'cols': 30,
            'rows': 10,
        })