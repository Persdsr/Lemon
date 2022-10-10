from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from .models import User

class RegisterUserForm(UserCreationForm):
    """Форма регистраций"""
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'forms__userName input-default', 'placeholder':'Логин'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'forms__userMail input-default', 'placeholder':'Почта'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'forms__userPass input-default', 'placeholder':'Пароль'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'forms__userPass input-default', 'placeholder':'Повтор пароля'}))

    field_order = ('username', 'email', 'password1', 'password2')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class StudyForm(UserChangeForm):
    """Форма настроек"""
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'forms__userName input-default', 'placeholder':'Логин'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'forms__userName input-default', 'placeholder':'Имя'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'forms__userName input-default', 'placeholder':'Фамилия'}))
    about_me = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'forms__userArea input-default', 'placeholder':'Обо мне'}))
    avatar = forms.ImageField(label='Аватарка', widget=forms.FileInput(attrs={'class': 'input-file-btn'}))
    profile_image = forms.ImageField(label='Изображение профиля', widget=forms.FileInput(attrs={'class': 'input-file-btn'}))
    password = None

    field_order = ('username', 'first_name', 'last_name', 'avatar', 'about_me', 'avatar', 'profile_image')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'avatar', 'about_me', 'avatar', 'profile_image')


class LoginUserForm(AuthenticationForm):
    """Форма логин"""
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'forms__userName input-default', 'placeholder': 'Логин'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'forms__userPass input-default', 'placeholder': 'Пароль'}))


class ContactForm(forms.ModelForm):
    """Форма рассылки"""
    model = Contact
    fields = '__all__'

