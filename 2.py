def wypisz_informacje(**kwargs):
    for klucz in kwargs :
        print(f'pod kluczem {klucz} znajduje się {kwargs[klucz]}. ')
wypisz_informacje(imie='Kacper', nazwisko='coś')