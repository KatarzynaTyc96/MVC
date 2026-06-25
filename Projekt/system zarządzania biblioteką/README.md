# System zarządzania biblioteką


## Spis treści

1. [Opis projektu]
2. [Zastosowanie wzorca MVC w Django]
3. [Funkcjonalności]
4. [Technologie]
5. [Struktura projektu]
6. [Wyszukiwanie i filtrowanie]
7. [Walidacja danych]
8. [Instrukcja uruchomienia]
9. [Autor]


## Opis projektu

Projekt to prosta aplikacja internetową do zarządzania biblioteką. Użytkownik może zapisywać książki, przeglądać listę pozycji, filtrować wyniki oraz edytować lub usuwać dane. Każda książka ma tytuł, autora, rok wydania, opis i datę dodania do systemu.

Aplikacja została przygotowana w Django. Kod podzielono zgodnie z założeniami MVC.


## Zastosowanie wzorca MVC w Django

- **Model**: `ksiazki/models.py`, klasa `Ksiazka`, pola `tytul`, `autor`, `rok_wydania`, `opis`, `data_dodania`.
- **Kontroler / logika obsługi żądań**: `ksiazki/views.py`, funkcje odpowiedzialne za listę, szczegóły, dodawanie, edycję i usuwanie książek.
- **Widok / szablony**: `ksiazki/templates/ksiazki/`, pliki HTML odpowiedzialne za wygląd stron.


## Funkcjonalności

- wyświetlanie listy książek,
- wyszukiwanie książek po tytule lub autorze,
- filtrowanie książek po autorze,
- filtrowanie książek po roku wydania,
- dodawanie nowej książki,
- edycja zapisanej książki,
- usuwanie książki,
- wyświetlanie szczegółów wybranej pozycji,
- komunikaty po dodaniu, edycji i usunięciu danych,
- panel administratora Django,
- przykładowe dane w pliku JSON.


## Technologie

- Python 3.14,
- Django 6.0.3,
- SQLite,
- HTML,
- CSS.


## Struktura projektu

system zarządzania biblioteką/
├── manage.py
├── requirements.txt
├── README.md
├── system_biblioteki/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── ksiazki/
    ├── models.py
    ├── forms.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    │   ├── __init__.py
    │   └── 0001_initial.py
    ├── fixtures/
    │   └── przykladowe_ksiazki.json
    ├── static/ksiazki/
    │   └── styl.css
    └── templates/ksiazki/
        ├── baza.html
        ├── lista_ksiazek.html
        ├── szczegoly_ksiazki.html
        ├── formularz_ksiazki.html
        └── potwierdzenie_usuniecia.html


## Wyszukiwanie i filtrowanie

Liste książek można filtrować. Filtry: `szukaj`, `autor` i `rok`.


## Walidacja danych

Dane są sprawdzane po stronie klienta oraz serwera.

Walidacja po stronie klienta wykorzystuje atrybuty formularzy HTML5, między innymi `required`, `minlength`, `maxlength`, `min`, `max` i `pattern`. Dzięki temu użytkownik od razu widzi podstawowe błędy w formularzu.

Walidacja po stronie serwera znajduje się w plikach `ksiazki/models.py` i `ksiazki/forms.py`. Aplikacja sprawdza, czy:

- tytuł jest wymagany i ma co najmniej 2 znaki,
- autor jest wymagany i ma co najmniej 3 znaki,
- rok wydania jest większy od 0 i nie jest późniejszy niż bieżący rok,
- opis nie przekracza 1000 znaków,
- pola tekstowe nie zawierają niedozwolonych znaków,
- ta sama książka nie została dodana drugi raz.


## Instrukcja uruchomienia

1. Pobierz projekt albo sklonuj repozytorium.

2. Przejdź do katalogu projektu:

```bash
cd "system zarządzania biblioteką"
```

3. Utwórz środowisko wirtualne:

```bash
python -m venv venv
```

4. Aktywuj środowisko wirtualne.

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Jeżeli PowerShell zablokuje uruchomienie skryptu, można użyć polecenia:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

5. Zainstaluj wymagane pakiety:

```powershell
python -m pip install -r requirements.txt
```
Po instalacji można sprawdzić wersje:

```powershell
python --version
python -m django --version
```


6. Wykonaj migracje bazy danych:

```bash
python manage.py migrate
```

7. Uruchom serwer developerski:

```bash
python manage.py runserver
```

8. Otwórz aplikację w przeglądarce:

```text
http://127.0.0.1:8000/
```

## Panel administratora

Aby zalogować się do panelu administratora, najpierw utwórz konto:

```bash
python manage.py createsuperuser
```

Po uruchomieniu serwera panel będzie dostępny pod adresem:

```text
http://127.0.0.1:8000/admin/
```

## Autor
 Katarzyna Tyc