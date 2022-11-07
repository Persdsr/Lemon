from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('food/<slug:food_slug>/', views.DetailFoodView.as_view(), name='detail_food'),
    path('<int:pk>/', views.save_favorite, name='favorite_post'),
    path('tags/<slug:tags_slug>/', views.HomeView.as_view(), name='tags_home'),
    path('category/<slug:category_slug>/', views.CategoryTagView.as_view(), name='category'),
    path('categories/', views.CategoryTagView.as_view(), name='categories'),
    path('favorite/', views.FavoriteView.as_view(), name='favorite'),
    path('account/', include('users.urls')),

    ##ajax
    path('update_favorite_status/<int:pk>/<slug:type>/', views.update_favorite_status, name='update_favorite_status'),
    path('update_comment_status/<int:pk>/<slug:type>/', views.update_comment_status, name='update_comment_status'),
]
