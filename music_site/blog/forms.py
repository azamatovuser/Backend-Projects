from django import forms
from .models import Comment_blog


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment_blog
        fields = "__all__"
        exclude = ['author', 'podcast', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({
            'class': 'comment_input comment_textarea', 'placeholder': 'Message',
        })