#!/usr/bin/env python
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'system_biblioteki.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Nie można zaimportować Django. Sprawdź, czy pakiet jest zainstalowany "
            "i dostępny w bieżącym środowisku Pythona."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
