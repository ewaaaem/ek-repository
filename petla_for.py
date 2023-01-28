#pętla for

#for i in range (10):
#    print(i,'Ewa')

#for i in range (0,10,1):
#    print(i,'pętla')

#for i in range (5,100,10):
#    print(i,'co 10')

#for i in range (100,10,-2):
#    print(i,'pętla')

#zadanie
#zsumuj wszystkie liczby parzyste od 0 do 100
sum=0
for i in range (101):
    if i%2 ==0:
        #sum= sum+i
        sum +=i
print(sum)

lista = [4, 15, 97, 64, 34, 26, 78, 50]
for i in range (len(lista)):
    if lista[i] <50:
        print(lista[i],' mniejsze od 50')
    elif lista[i] >50:
        print(lista[i], ' większe od 50')
    else:
        print(lista[i], ' równe 50')
