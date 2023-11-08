from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Slowko, ZnajomoscSlowka
from django.views.decorators.http import require_POST
from django.forms.models import model_to_dict
from django.http import JsonResponse
import json
from django.core.serializers.json import DjangoJSONEncoder



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
def powtarzanie_view(request):
    return render(request, 'powtarzanie.html')


@login_required
def nauka_view(request):
    slowka_ktorych_uzytkownik_nie_zna = ZnajomoscSlowka.objects.filter(
        user=request.user,
        zna=False
    ).select_related('slowko')

    slowka_do_nauki = [
        {
            'id': znajomosc.slowko.id,
            'polskie': znajomosc.slowko.polskie,
            'angielskie': znajomosc.slowko.angielskie
        } for znajomosc in slowka_ktorych_uzytkownik_nie_zna
    ]

    # Używamy DjangoJSONEncoder do bezpiecznego konwertowania na JSON
    slowka_do_nauki_json = json.dumps(slowka_do_nauki, cls=DjangoJSONEncoder)

    return render(request, 'nauka.html', {'slowka_do_nauki_json': slowka_do_nauki_json})

@login_required
@require_POST
def update_znajomosc_slowka(request):
    slowko_id = request.POST.get('slowko_id')
    if slowko_id:
        znajomosc, created = ZnajomoscSlowka.objects.get_or_create(user=request.user, slowko_id=slowko_id, defaults={'zna': True})
        if not created:
            znajomosc.zna = True
            znajomosc.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


@login_required
def powtarzanie_view(request):
    slowka_do_powtorki = ZnajomoscSlowka.objects.filter(user=request.user, zna=True).select_related('slowko')
    slowka_do_powtorki_json = json.dumps(
        [model_to_dict(znajomosc.slowko, fields=['id', 'angielskie', 'polskie']) for znajomosc in slowka_do_powtorki],
        cls=DjangoJSONEncoder
    )
    return render(request, 'powtarzanie.html', {'slowka_do_powtorki_json': slowka_do_powtorki_json})