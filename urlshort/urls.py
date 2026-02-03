from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.createShortURL, name='create'),
    path('my-urls/', views.my_urls, name='my_urls'),
    path('edit/<int:url_id>/', views.edit_url, name='edit_url'),
    path('delete/<int:url_id>/', views.delete_url, name='delete_url'),
    
    # auth urls
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    
    # this should be last so it doesnt catch other urls
    path('<str:url>/', views.redirect_url, name='redirect_url'),
]
