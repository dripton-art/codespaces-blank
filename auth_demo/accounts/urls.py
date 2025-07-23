from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('secret/', views.secret_page, name='secret'),
    path('logout/', CustomLogoutView.as_view(next_page='login'), name='logout'),
]
