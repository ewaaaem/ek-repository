
dane = input('Wpisz imię, nazwisko i wiek, oddzielając gwiazdką').split('*')
print('Cześć', dane[0],'. Masz', dane[2], 'lat')

dane = input('Wpisz imię, nazwisko i wiek, oddzielając spacją').split()
print('Cześć', dane[0],'. Masz', dane[2], 'lat')

wyplata = int(input('Wpisz wypłatę'))
if wyplata <= 5000:
    print('Gratulacje')
    print('Wysłanie maila')
print('Kolejna instrukcja')
