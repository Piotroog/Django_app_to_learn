from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, home, logout_request #, nauka_view
from aplikacja_ang import views
from .views import update_znajomosc_slowka




urlpatterns = [
    path('login/', views.login_view, name='login'), #login
    path('signup/', SignUpView.as_view(), name='signup'),#signup
    path('home/', home, name='home'), #home
    path('nauka/', views.nauka_view, name='nauka'), #nauka
    path('powtarzanie', views.powtarzanie_view, name='powtarzanie'), #powtarzanie
    path('logout/', logout_request, name='logout'), #logout
    path('update_znajomosc_slowka/', update_znajomosc_slowka, name='update_znajomosc_slowka'),
]
