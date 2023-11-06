from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Slowko, ZnajomoscSlowka

def login_view(request):  #Logowanie
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Przekieruj do strony głównej po zalogowaniu.
            else:
                return HttpResponse("Nieudane logowanie. Spróbuj ponownie.", status=401)
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

class SignUpView(generic.CreateView):  #Przekierowuje do URL logowania po pomyślnej rejestracji
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Przekierowuje do URL logowania po pomyślnej rejestracji
    template_name = 'signup.html'

@login_required  # Dekorator wymusza, aby tylko zalogowani użytkownicy mieli dostęp do tego widoku
def home(request):
    return render(request, 'home.html')
@login_required
def nauka_view(request):
    # Pobieramy wszystkie słówka bezpośrednio z modelu Slowko.
    wszystkie_slowka = Slowko.objects.all()
    return render(request, 'nauka.html', {'slowka_do_nauki': wszystkie_slowka})
@login_required
def powtarzanie_view(request):
    return render(request, 'powtarzanie.html')