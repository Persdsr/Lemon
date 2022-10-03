from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Comment


class CommentForm(forms.ModelForm):
    """Форма комментов"""
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Текст комментария', 'class': 'comments__usertext'})
        }

