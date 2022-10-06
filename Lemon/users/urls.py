from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('settings/', views.edit_settings, name='settings'),
    path('logout/', views.Logout, name='logout'),
]
