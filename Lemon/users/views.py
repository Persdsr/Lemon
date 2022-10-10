from food.models import Post

from .models import User
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView
from django.contrib.auth.forms import UserChangeForm

from .forms import LoginUserForm, RegisterUserForm, StudyForm, ContactForm


class LoginUserView(LoginView):
    """Логин"""
    form_class = LoginUserForm
    template_name = 'user/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUserView(CreateView):
    """Регистрация"""
    template_name = 'user/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        form = RegisterUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(self.request, user)
            return redirect('home')
        else:
            return render(request, self.template_name, {'form': form})


def edit_settings(request):
    """Настройки"""
    if request.method == 'POST':
        form = StudyForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudyForm(instance=request.user)

    args = {'form': form}
    return render(request, 'user/study.html', args)


def about_me(request, profile_pk, profile_slug):
    """Профиль"""
    user = get_object_or_404(User, pk=profile_pk)
    posts = Post.objects.filter(author=user).select_related('category')

    if profile_slug == 'posts':
        return render(request, 'user/profile/profile_posts.html', {'profile': user,'posts': posts})

    return render(request, 'user/profile/about_me.html', {'profile': user, 'posts': posts})


def Logout(request):
    logout(request)
    return redirect('home')


class ContactView(CreateView):
    """Рассылка сообщений"""
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'user/contact.html'

    def form_valid(self, form):
        form.save()
        send(form.instance.email)
        return super().form_valid(form)