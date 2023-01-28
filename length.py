
#wyświetlenie typu i długości danych
a=5
b='Diana'
print(type(b))
print(len(b))

x= input('Wpisz imie ')
print('Czesc',x,'masz',a,'lat')

wiek = int(input('Ile masz lat? '))
#wiek = int(wiek) (alternatywny sposób zamiany danych na int)
czas_do_18 = 18 - wiek
print ('Będziesz pełnoletni za', czas_do_18, 'lat')
