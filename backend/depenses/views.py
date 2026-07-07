from django.shortcuts import render, redirect
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from .forms import DepenseForm
from .models import Depense
from django.http import JsonResponse


@login_required(login_url='login')
def liste_depenses(request, id=None):
    if request.method == "GET":
        if id:
            depense = Depense.objects.get(id=id)
            edit_form = DepenseForm(instance=depense)
            form = DepenseForm()
        else:
            form = DepenseForm()
            edit_form = None

        # --- Base queryset ---
        depenses = Depense.objects.all()

        # --- Recherche par titre ---
        recherche = request.GET.get('q', '').strip()
        if recherche:
            depenses = depenses.filter(titre__icontains=recherche)

        # --- Filtre catégorie ---
        categorie = request.GET.get('categorie', '')
        if categorie:
            depenses = depenses.filter(categorie=categorie)

        # --- Filtre période ---
        periode = request.GET.get('periode', 'ce_mois')
        aujourdhui = timezone.now().date()

        if periode == 'ce_mois':
            depenses = depenses.filter(date__year=aujourdhui.year, date__month=aujourdhui.month)
        elif periode == 'mois_dernier':
            mois_dernier = (aujourdhui.replace(day=1) - timedelta(days=1))
            depenses = depenses.filter(date__year=mois_dernier.year, date__month=mois_dernier.month)
        elif periode == 'tout':
            pass  # pas de filtre

        depenses = depenses.order_by('-date')

        # --- Stats ---
        total = depenses.aggregate(Sum('montant'))['montant__sum'] or 0

        # Comparaison vs mois dernier (seulement pertinent si on regarde "ce_mois")
        mois_dernier_date = (aujourdhui.replace(day=1) - timedelta(days=1))
        total_mois_dernier = Depense.objects.filter(
            date__year=mois_dernier_date.year,
            date__month=mois_dernier_date.month
        ).aggregate(Sum('montant'))['montant__sum'] or 0

        if total_mois_dernier > 0:
            variation = round(((total - total_mois_dernier) / total_mois_dernier) * 100)
        else:
            variation = None

        contexte = {
            'donnee': depenses,
            'form': form,
            'edit_form': edit_form,
            'total': total,
            'id': id,
            'active_page': 'depenses',
            'recherche': recherche,
            'categorie_selectionnee': categorie,
            'periode_selectionnee': periode,
            'variation': variation,
            'categories': Depense.CATEGORIES,
        }

        # Requête HTMX (navigation interne) → on ne renvoie que le fragment,
        # pas toute la page avec la sidebar
        est_fragment = request.headers.get('HX-Request') and not request.headers.get('HX-Boosted')
        template = 'depenses/liste_content.html' if est_fragment else 'depenses/liste.html'
        return render(request, template, contexte)

    elif request.method == "POST":
        if 'delete' in request.POST:
            Depense.objects.get(id=id).delete()
            return redirect('liste_depenses')

        if 'edit' in request.POST:
            depense = Depense.objects.get(id=id)
            form = DepenseForm(request.POST, instance=depense)
            if form.is_valid():
                form.save()
                return redirect('liste_depenses')

        else:
            form = DepenseForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('liste_depenses')


@login_required(login_url='login')
def get_depense(request, id):
    depense = Depense.objects.get(id=id)
    return JsonResponse({
        'titre': depense.titre,
        'montant': str(depense.montant),
        'categorie': depense.categorie,
        'description': depense.description,
    })