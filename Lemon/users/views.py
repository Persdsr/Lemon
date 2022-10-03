from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserChangeForm

from .forms import LoginUserForm, RegisterUserForm, StudyForm


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'user/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUserView(CreateView):
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


def edit_profile(request):
    if request.method == 'POST':
        form = StudyForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudyForm(instance=request.user)

    args = {'form': form}
    return render(request, 'user/study.html', args)


def Logout(request):
    logout(request)
    return redirect('home')