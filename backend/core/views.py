from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta
from .forms import LoginForm

from depenses.models import Depense


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


MOIS_COURT = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun', 'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc']


def _mois_precedent(date_ref, n):
    """Retourne (année, mois) n mois avant date_ref."""
    annee = date_ref.year
    mois = date_ref.month - n
    while mois <= 0:
        mois += 12
        annee -= 1
    return annee, mois


@login_required(login_url='login')
def resume(request):
    aujourdhui = timezone.now().date()
    debut_mois = aujourdhui.replace(day=1)
    annee_dernier, mois_dernier = _mois_precedent(aujourdhui, 1)

    # --- KPIs du mois en cours ---
    depenses_mois = Depense.objects.filter(
        date__year=aujourdhui.year, date__month=aujourdhui.month
    )
    total_mois = depenses_mois.aggregate(Sum('montant'))['montant__sum'] or 0
    nb_depenses_mois = depenses_mois.count()

    total_mois_dernier = Depense.objects.filter(
        date__year=annee_dernier, date__month=mois_dernier
    ).aggregate(Sum('montant'))['montant__sum'] or 0

    if total_mois_dernier > 0:
        variation = round(((total_mois - total_mois_dernier) / total_mois_dernier) * 100)
    else:
        variation = None

    moyenne_jour = round(total_mois / aujourdhui.day) if aujourdhui.day else 0

    # --- Répartition par catégorie (mois en cours) ---
    categories_dict = dict(Depense.CATEGORIES)
    repartition_qs = (
        depenses_mois.values('categorie')
        .annotate(total=Sum('montant'))
        .order_by('-total')
    )
    repartition = [
        {'categorie': categories_dict.get(item['categorie'], item['categorie']), 'total': item['total']}
        for item in repartition_qs
    ]
    categorie_principale = repartition[0]['categorie'] if repartition else '—'

    chart_cat_labels = [item['categorie'] for item in repartition]
    chart_cat_data = [float(item['total']) for item in repartition]

    # --- Évolution sur les 6 derniers mois ---
    evolution = []
    for i in range(5, -1, -1):
        annee, mois = _mois_precedent(aujourdhui, i)
        total = Depense.objects.filter(
            date__year=annee, date__month=mois
        ).aggregate(Sum('montant'))['montant__sum'] or 0
        evolution.append({'label': MOIS_COURT[mois - 1], 'total': float(total)})

    chart_evo_labels = [item['label'] for item in evolution]
    chart_evo_data = [item['total'] for item in evolution]

    # --- Dernières dépenses ---
    dernieres_depenses = Depense.objects.all().order_by('-date', '-id')[:5]

    contexte = {
        'active_page': 'resume',
        'total_mois': total_mois,
        'variation': variation,
        'nb_depenses_mois': nb_depenses_mois,
        'moyenne_jour': moyenne_jour,
        'categorie_principale': categorie_principale,
        'repartition': repartition,
        'dernieres_depenses': dernieres_depenses,
        'chart_cat_labels': chart_cat_labels,
        'chart_cat_data': chart_cat_data,
        'chart_evo_labels': chart_evo_labels,
        'chart_evo_data': chart_evo_data,
    }

  
    est_fragment = request.headers.get('HX-Request') and not request.headers.get('HX-Boosted')
    template = 'core/resume_content.html' if est_fragment else 'core/resume.html'
    return render(request, template, contexte)