from django.shortcuts import render, redirect
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
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

        depenses = Depense.objects.all()
        total = depenses.aggregate(Sum('montant'))['montant__sum'] or 0

        return render(request, 'depenses/liste.html', {
            'donnee': depenses,
            'form': form,
            'edit_form': edit_form,
            'total': total,
            'id': id,
        })

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