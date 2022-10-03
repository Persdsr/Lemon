from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('profile/', views.edit_profile, name='profile'),
    path('logout/', views.Logout, name='logout'),
]
