from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('login')), 
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]