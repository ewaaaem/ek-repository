#Program prosi o imię, wiek i wypłatę
#Program pisze "cześć", albo "dzień dobry" w zależności od wieku
#Program wypisuje podatek do zapłaty (15% wypłaty).

#else
dane=input('Podaj imię, wiek i wypłatę oddzielając dane spacją').split()
if int(dane[1]) <= 18:
    print('Cześć', dane[0])
else:
    print ('Dzień dobry', dane[0])

podatek=0.15*int(dane[-1])
print('Zapłacisz podatek:', podatek)

#dane=input('Podaj imię, wiek i wypłatę oddzielając dane spacją').split()
#if int(dane[1]) <= 18:
#    print('Cześć', dane[0])
#if int(dane[1]) < 18:
#    print('Dzień dobry', dane[0])

#podatek=0.15*int(dane[-1])
#print('Zapłacisz podatek:', podatek)

#elif
dane=input('Podaj imię, wiek i wypłatę oddzielając dane spacją').split()
if int(dane[1]) <= 18 and int(dane[1]) > 0 :
    print('Cześć', dane[0])
elif int(dane[1]) > 18:
    print('Dzień dobry', dane[0])
else:
    print("Zły wiek")
podatek=0.15*int(dane[-1])
print('Zapłacisz podatek:', podatek)
