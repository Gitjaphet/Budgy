from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django_tenants.utils import schema_context
from .models import Tenant, Domain
from .forms import InscriptionForm, FindTenantForm


def inscription(request):

    if request.tenant.schema_name != 'public':
        return redirect('dashboard')

    form = InscriptionForm()

    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom_organisation']
            email = form.cleaned_data['email']
            telephone = form.cleaned_data['telephone']
            mot_de_passe = form.cleaned_data['mot_de_passe']

            # Vérifier que le sous-domaine n'existe pas déjà
            domaine_complet = f"{nom}.budgy.artjatie.com"
            if Domain.objects.filter(domain=domaine_complet).exists():
                form.add_error('nom_organisation', "Ce nom d'organisation est déjà pris.")
                return render(request, 'tenants/inscription.html', {'form': form})

            # Créer le tenant → crée automatiquement le schema PostgreSQL
            tenant = Tenant(schema_name=nom, nom=nom, email=email)
            tenant.save()

            # Créer le domaine
            domain = Domain(domain=domaine_complet, tenant=tenant, is_primary=True)
            domain.save()

            # Créer l'utilisateur admin dans le schema du tenant
            with schema_context(nom):
                user = User.objects.create_user(
                    username=email,
                    email=email,
                    password=mot_de_passe,
                    first_name=nom,
                )
                user.save()

            # Rediriger vers le sous-domaine du tenant
            return redirect(f"https://{domaine_complet}/")

    return render(request, 'tenants/inscription.html', {'form': form})


def login_public(request):
    if request.tenant.schema_name != 'public':
        return redirect('dashboard')

    form = FindTenantForm()

    if request.method == 'POST':
        form = FindTenantForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            try:
                tenant = Tenant.objects.get(email=email)
                domain = tenant.domains.filter(is_primary=True).first()
                return redirect(f"https://{domain.domain}/login/")
            except Tenant.DoesNotExist:
                form.add_error('email', "Aucun espace trouvé avec cet email.")

    return render(request, 'tenants/login_public.html', {'form': form})