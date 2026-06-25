from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


walidator_pola_tekstowego = RegexValidator(
    regex=r"^[A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż0-9 .,:;!?'()\-]+$",
    message='Pole zawiera niedozwolone znaki.'
)

walidator_opisu = RegexValidator(
    regex=r"^[A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż0-9 .,:;!?'()\-\n\r]+$",
    message='Opis zawiera niedozwolone znaki.'
)


def waliduj_rok_wydania(wartosc):
    obecny_rok = date.today().year
    if wartosc < 1:
        raise ValidationError('Rok wydania musi być większy od 0.')
    if wartosc > obecny_rok:
        raise ValidationError('Rok wydania nie może być z przyszłości.')


class Ksiazka(models.Model):
    tytul = models.CharField(
        'Tytuł',
        max_length=200,
        validators=[MinLengthValidator(2, 'Tytuł musi mieć co najmniej 2 znaki.'), walidator_pola_tekstowego]
    )
    autor = models.CharField(
        'Autor',
        max_length=200,
        validators=[MinLengthValidator(3, 'Autor musi mieć co najmniej 3 znaki.'), walidator_pola_tekstowego]
    )
    rok_wydania = models.PositiveIntegerField('Rok wydania', validators=[waliduj_rok_wydania])
    opis = models.TextField(
        'Opis',
        blank=True,
        max_length=1000,
        validators=[walidator_opisu]
    )
    data_dodania = models.DateTimeField('Data dodania', auto_now_add=True)

    class Meta:
        ordering = ['tytul']
        verbose_name = 'Książka'
        verbose_name_plural = 'Książki'
        constraints = [
            models.UniqueConstraint(
                fields=['tytul', 'autor', 'rok_wydania'],
                name='unikalna_ksiazka_tytul_autor_rok'
            )
        ]

    def clean(self):
        super().clean()
        if self.tytul and self.autor and self.tytul.strip().lower() == self.autor.strip().lower():
            raise ValidationError('Tytuł książki nie powinien być taki sam jak autor.')

    def __str__(self):
        return f'{self.tytul} - {self.autor}'
