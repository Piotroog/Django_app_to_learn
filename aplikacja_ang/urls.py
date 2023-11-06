from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView
from aplikacja_ang import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
