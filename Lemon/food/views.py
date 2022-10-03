from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin

from .forms import CommentForm
from .models import Post, Comment, PostView, Tags, SeasonPost
from users.forms import RegisterUserForm, LoginUserForm


class HomeView(ListView):
    """Главная страница"""
    model = Post
    template_name = 'food/index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tags.objects.all()
        context['seasons'] = SeasonPost.objects.all()
        return context

    def get_queryset(self):
        """Изменения квери если в запросе есть теги"""
        if self.kwargs.get('tags_slug'):
            post = Post.objects.order_by('?').filter(tags__slug=self.kwargs.get('tags_slug')).order_by('-date_create')
        elif 'name' in self.request.GET:
            post = Post.objects.filter(Q(title__in=self.request.GET.getlist('name')) | (Q(title__iregex=self.request.GET.get('name'))))
        else:
            post = Post.objects.order_by('-date_create')
        return post


def save_favorite(request, pk):
    """Сохранить избранные посты"""
    user = request.user
    user.favorite_posts.add(Post.objects.get(id=pk))
    context = {
        'tags': Tags.objects.all(),
        'seasons': SeasonPost.objects.all(),
        'posts': Post.objects.all()
    }
    return render(request, 'food/index.html', context)


class DetailFoodView(DetailView, FormMixin):
    """детейл для поста"""
    model = Post
    template_name = 'food/detail_food.html'
    context_object_name = 'post'
    slug_url_kwarg = 'food_slug'
    form_class = CommentForm

    def get_object(self):
        """Функция для подсчета просмотров через логин клиента или через его IP"""
        post = Post.objects.get(slug=self.kwargs['food_slug'])
        if self.request.user.is_authenticated:
            user = self.request.user

            user.post_views.add(Post.objects.get(id=post.id))
        return post

    def post(self, request, *args, **kwargs):
        """Отправка комментов"""
        if request.user.is_authenticated:
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        else:
            return redirect('login')

    def form_valid(self, form):
        """Заполнение объектов в форму модели"""
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('detail_food', kwargs={'food_slug': self.get_object().slug})

def update_favorite_status(request, pk, type):
    """Изменение с избранными постами"""
    user = request.user
    if type == 'delete':
        user.favorite_posts.remove(Post.objects.get(pk=pk))

def update_comment_status(request, pk, type):
    """Изменение с избранными постами"""
    comment = Comment.objects.get(pk=pk)
    if request.user.is_superuser or request.user == comment.author:
        if type == 'delete':
            comment.delete()

class FavoriteView(ListView):
    """Страница с избранными постами"""
    template_name = 'food/favorite.html'
    queryset = Post
    context_object_name = 'posts'

    def get_queryset(self):
        posts = self.request.user.favorite_posts.all()
        return posts

