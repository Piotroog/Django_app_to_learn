from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, home, logout_request #, nauka_view
from aplikacja_ang import views





urlpatterns = [
    path('login/', views.login_view, name='login'), #login
    path('signup/', SignUpView.as_view(), name='signup'),#signup
    path('home/', home, name='home'), #home
    path('nauka/', views.nauka_view, name='nauka'),
    path('powtarzanie', views.powtarzanie_view, name='powtarzanie'),
    path('logout/', logout_request, name='logout'),
]
