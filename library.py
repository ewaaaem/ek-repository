import os
import time
#jeśli zaimportuję bibliotekę poprzez
#from time import * - zaczytuje wszystko z tej biblioteki i nie trzeba mówić skąd się bierze funkcję


#pokazuje jakie funkcje dana biblioteka posiada
#print(dir(os))


#odwołanie sie do biblioteki
path = os.getcwd()
print (path)

#zmiana ścieżki
#przy ścieżkach musi być dwa razy \\, bo jeden \ mówi, że będzie znak specjalny
#a drugi \ mówi, że ten znak spacjalny to \
os.chdir('C:\\Users\\Ewa\\Desktop')
print (os.getcwd())
#alternatywna komenda do zmiany ścieżki
#os.system('cmd /c "cd C:\\Users\\Ewa\\Desktop"') - czyli wejdź w command line i przejdź do ścieżki


#tworzenie folderu
os.mkdir('new_folder')
time.sleep(4)
#zmiana nazwy
os.rename('new_folder', 'new_folder2')
time.sleep(4)
#usunięcie folderu
os.rmdir('new_folder2')




