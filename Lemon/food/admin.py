from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms

from .models import Post, PostStep, Comment, Tags, SeasonPost, Category


class PostStepInline(admin.StackedInline):
    model = PostStep
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'get_photo_url', 'id']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PostStepInline]

    def get_photo_url(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=200px; height=150px;>")


@admin.register(SeasonPost)
class SeasonPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'get_photo_url', 'id']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PostStepInline]

    def get_photo_url(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=200px; height=150px;>")

@admin.register(PostStep)
class PostStepAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class PostStepAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
