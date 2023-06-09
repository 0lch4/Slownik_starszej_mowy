# Słownik starszej mowy

![GitHub forks](https://img.shields.io/badge/Version-1.1.0-red)

Interface in Polish lang

# Opis

Słownik internetowy wykorzystujący bazę danych MySQL oraz FastApi, który po wprowadzeniu Polskiego słowa wyszukuje jego odpowiednik w starszej mowie z Wiedźmina.

## Licencja

Aplikacja działa na licencji MIT

# Instalacja

Wymagany jest serwer [MySQL](https://dev.mysql.com/downloads/mysql/)

## Kopiowanie repozytorium:

```
git clone https://github.com/0lch4/Slownik_starszej_mowy.git
```

## Instalacja bibliotek:

Wymagane jest narzędzie `poetry`:

```
pip install poetry
```

Następnie w głównej lokalizacji wpisujemy

```
poetry install
```

## Plik .env:

Należy stworzyć plik `.env` na podstawie `.env.example`

## Ładowanie danych do bazy

Należy uruchomić skrypt `load_data_to_database.sh` z poziomu głownego folderu
```
./app/load_data_to_database.sh
```

Osoby, które nie mają linuxa/git basha muszą stworzyć folder dictionaries w folderze load_data następnie z głównej lokalizacji:

```
python -m app.load_data
```

# Uruchamianie

Gdy wszystkie zależności zostały spełnione wpisujemy w głównej lokalizacji:

```
uvicorn app.main:app --reload
```

Aplikacja będzie dostępna pod adresem:

```
http://localhost:8000/
```

## Uruchamianie w kontenerze

Aby uruchomić kontener należy wpisać w głównej lokalizacji:

```
docker-compose up --build
```

Aplikacja będzie dostępna pod adresem:

```
http://localhost:8000/
```

# Zrzuty ekranu

![screen1](screenshots/screen1.png)
![screen2](screenshots/screen2.png)

# Źródła

https://wiedzmin.fandom.com/wiki/S%C5%82ownik_starszej_mowy
