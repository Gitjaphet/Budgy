from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm


def login_view(request):
    if request.tenant.schema_name == 'public':
        return redirect('login_public')

    if request.user.is_authenticated:
        return redirect('dashboard')

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            mot_de_passe = form.cleaned_data['mot_de_passe']

            user = authenticate(request, username=email, password=mot_de_passe)

            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')
            else:
                form.add_error(None, "Email ou mot de passe incorrect.")

    return render(request, 'core/login.html', {'form': form})


def logout_view(request):
    auth_logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'core/dashboard.html')