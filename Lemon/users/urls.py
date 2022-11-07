from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/<slug:user_slug>/<slug:profile_slug>/', views.about_me, name='about_me'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('settings/', views.edit_settings, name='settings'),
    path('logout/', views.Logout, name='logout'),
]
