#1. Odczyt pliku csv z zapisem poszczegolnych pol

path = 'C:\Users\Ewa\Desktop\\rozliczenie.csv'
mode = 'r'

with open(path, mode) as plik2:
    content = plik2.readlines()
# print(content[3])
for i in range(len(content)):
    # print(content[i])
    content[i] = content[i].split(',')
#     print(content[i])
# print(content[2][2])

# 2. Obliczanie sredniej wyplaty

total = 0
for i in range(1, len(content)):
    print(content[i][1])
    total = total + int(content[i][1])
print('Suma wynagrodzen: ', total)
average = total / (len(content)-1)
print('Srednia wynagrodzen: ', round(average, 2))

# 3. Obliczanie liczby kobiet na macierzynskim

total = 0
for i in range(1,len(content)):
    print(content[i])
    content[i][4] = content[i][4].replace('\n', '')
    if content[i][4] == 't' and content[i][3] == 'k':
        total += 1
print(total)
