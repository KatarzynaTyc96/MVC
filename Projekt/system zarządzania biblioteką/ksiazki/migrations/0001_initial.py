from django.core.validators import MinLengthValidator
from django.db import migrations, models
import ksiazki.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Ksiazka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=200, validators=[MinLengthValidator(2, 'Tytuł musi mieć co najmniej 2 znaki.'), ksiazki.models.walidator_pola_tekstowego], verbose_name='Tytuł')),
                ('autor', models.CharField(max_length=200, validators=[MinLengthValidator(3, 'Autor musi mieć co najmniej 3 znaki.'), ksiazki.models.walidator_pola_tekstowego], verbose_name='Autor')),
                ('rok_wydania', models.PositiveIntegerField(validators=[ksiazki.models.waliduj_rok_wydania], verbose_name='Rok wydania')),
                ('opis', models.TextField(blank=True, max_length=1000, validators=[ksiazki.models.walidator_opisu], verbose_name='Opis')),
                ('data_dodania', models.DateTimeField(auto_now_add=True, verbose_name='Data dodania')),
            ],
            options={
                'verbose_name': 'Książka',
                'verbose_name_plural': 'Książki',
                'ordering': ['tytul'],
            },
        ),
        migrations.AddConstraint(
            model_name='ksiazka',
            constraint=models.UniqueConstraint(
                fields=('tytul', 'autor', 'rok_wydania'),
                name='unikalna_ksiazka_tytul_autor_rok'
            ),
        ),
    ]
