
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    #path('login/', auth_views.LoginView.as_view(template_name='aplikacja_ang/login.html'), name='login'),
]
