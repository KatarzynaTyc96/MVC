from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import KsiazkaForm
from .models import Ksiazka


def lista_ksiazek(request):
    szukaj = request.GET.get('szukaj', '').strip()
    autor = request.GET.get('autor', '').strip()
    rok = request.GET.get('rok', '').strip()

    ksiazki = Ksiazka.objects.all()

    if szukaj:
        ksiazki = ksiazki.filter(Q(tytul__icontains=szukaj) | Q(autor__icontains=szukaj))
    if autor:
        ksiazki = ksiazki.filter(autor__icontains=autor)
    if rok.isdigit():
        ksiazki = ksiazki.filter(rok_wydania=int(rok))

    autorzy = Ksiazka.objects.order_by('autor').values_list('autor', flat=True).distinct()

    return render(request, 'ksiazki/lista_ksiazek.html', {
        'ksiazki': ksiazki,
        'szukaj': szukaj,
        'autor': autor,
        'rok': rok,
        'autorzy': autorzy,
    })


def szczegoly_ksiazki(request, pk):
    ksiazka = get_object_or_404(Ksiazka, pk=pk)
    return render(request, 'ksiazki/szczegoly_ksiazki.html', {'ksiazka': ksiazka})


def dodaj_ksiazke(request):
    if request.method == 'POST':
        formularz = KsiazkaForm(request.POST)
        if formularz.is_valid():
            formularz.save()
            messages.success(request, 'Książka została dodana.')
            return redirect('lista_ksiazek')
    else:
        formularz = KsiazkaForm()

    return render(request, 'ksiazki/formularz_ksiazki.html', {
        'formularz': formularz,
        'naglowek': 'Dodaj książkę',
    })


def edytuj_ksiazke(request, pk):
    ksiazka = get_object_or_404(Ksiazka, pk=pk)

    if request.method == 'POST':
        formularz = KsiazkaForm(request.POST, instance=ksiazka)
        if formularz.is_valid():
            formularz.save()
            messages.success(request, 'Dane książki zostały zaktualizowane.')
            return redirect('szczegoly_ksiazki', pk=ksiazka.pk)
    else:
        formularz = KsiazkaForm(instance=ksiazka)

    return render(request, 'ksiazki/formularz_ksiazki.html', {
        'formularz': formularz,
        'naglowek': 'Edytuj książkę',
    })


def usun_ksiazke(request, pk):
    ksiazka = get_object_or_404(Ksiazka, pk=pk)

    if request.method == 'POST':
        ksiazka.delete()
        messages.success(request, 'Książka została usunięta.')
        return redirect('lista_ksiazek')

    return render(request, 'ksiazki/potwierdzenie_usuniecia.html', {'ksiazka': ksiazka})
