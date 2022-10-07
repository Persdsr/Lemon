from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import inlineformset_factory

from .models import Comment, Post, PostStep


class CommentForm(forms.ModelForm):
    """Форма комментов"""
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Текст комментария', 'class': 'comments__usertext'})
        }

class CreateRecipesForm(forms.ModelForm):
    """Форма создания рецепта"""

    class Meta:
        #https://www.youtube.com/watch?v=MRWFg30FmZQ
        model = inlineformset_factory(Post, PostStep, fields=('title',))
        exclude = ('author', 'date_create', 'views', 'favorite')
