from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Slowko, ZnajomoscSlowka
from django.views.decorators.http import require_POST

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

@login_required
@require_POST
def logout_request(request):
    logout(request)
    return redirect(reverse('login'))

class SignUpView(generic.CreateView):  #Przekierowuje do URL logowania po pomyślnej rejestracji
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Przekierowuje do URL logowania po pomyślnej rejestracji
    template_name = 'signup.html'

@login_required  # Dekorator wymusza, aby tylko zalogowani użytkownicy mieli dostęp do tego widoku
def home(request):
    return render(request, 'home.html')
@login_required
def nauka_view(request):
    # Pobieramy wszystkie słówka bezpośrednio z modelu Slowko.   DO SPRAWDZENIA
    wszystkie_slowka = Slowko.objects.all()
    return render(request, 'nauka.html', {'slowka_do_nauki': wszystkie_slowka})
@login_required
def powtarzanie_view(request):
    return render(request, 'powtarzanie.html')


# @login_required
# def nauka_view(request):    #DO SPRAWDZENIA
#     # Pobierz wszystkie Słówka, których użytkownik nie zna
#     slowka_ktorych_uzytkownik_nie_zna = ZnajomoscSlowka.objects.filter(user=request.user, zna=False)
#
#     # Pobierz obiekty Slowko powiązane z ZnajomoscSlowka
#     slowka_do_nauki = [znajomosc.slowko for znajomosc in slowka_ktorych_uzytkownik_nie_zna]
#
#     return render(request, 'nauka.html', {'slowka_do_nauki': slowka_do_nauki})


