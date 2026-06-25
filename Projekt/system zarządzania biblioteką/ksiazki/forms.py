from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from .models import Ksiazka


class KsiazkaForm(forms.ModelForm):
    class Meta:
        model = Ksiazka
        fields = ['tytul', 'autor', 'rok_wydania', 'opis']
        widgets = {
            'tytul': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'np. Lalka',
                'required': True,
                'minlength': 2,
                'maxlength': 200,
                'pattern': r"[A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż0-9 .,:;!?'()\-]+",
                'title': 'Tytuł może zawierać litery, cyfry, spacje i podstawowe znaki interpunkcyjne.'
            }),
            'autor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'np. Bolesław Prus',
                'required': True,
                'minlength': 3,
                'maxlength': 200,
                'pattern': r"[A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż0-9 .,:;!?'()\-]+",
                'title': 'Autor może zawierać litery, cyfry, spacje i podstawowe znaki interpunkcyjne.'
            }),
            'rok_wydania': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'np. 1890',
                'required': True,
                'min': 1,
                'max': date.today().year
            }),
            'opis': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Krótki opis książki',
                'maxlength': 1000
            }),
        }

    def clean_tytul(self):
        tytul = self.cleaned_data['tytul'].strip()
        if len(tytul) < 2:
            raise ValidationError('Tytuł musi mieć co najmniej 2 znaki.')
        return tytul

    def clean_autor(self):
        autor = self.cleaned_data['autor'].strip()
        if len(autor) < 3:
            raise ValidationError('Autor musi mieć co najmniej 3 znaki.')
        return autor

    def clean_rok_wydania(self):
        rok = self.cleaned_data['rok_wydania']
        if rok < 1:
            raise ValidationError('Rok wydania musi być większy od 0.')
        if rok > date.today().year:
            raise ValidationError('Rok wydania nie może być z przyszłości.')
        return rok

    def clean_opis(self):
        opis = self.cleaned_data.get('opis', '').strip()
        if len(opis) > 1000:
            raise ValidationError('Opis może mieć maksymalnie 1000 znaków.')
        return opis

    def clean(self):
        cleaned_data = super().clean()
        tytul = cleaned_data.get('tytul')
        autor = cleaned_data.get('autor')
        rok = cleaned_data.get('rok_wydania')

        if tytul and autor and rok:
            podobne = Ksiazka.objects.filter(
                tytul__iexact=tytul,
                autor__iexact=autor,
                rok_wydania=rok
            )
            if self.instance.pk:
                podobne = podobne.exclude(pk=self.instance.pk)
            if podobne.exists():
                raise ValidationError('Taka książka jest już zapisana w bibliotece.')
        return cleaned_data
