from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

def login_view(request):
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
# Create your views here.
