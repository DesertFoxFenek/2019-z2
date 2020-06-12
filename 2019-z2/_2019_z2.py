import os   #cls do czyszczenia ekranu
import sys  #do użycia exit(0) w celu zakończeni programu

def odczyt():

    try:
        tekst = []
        tekst = open("lista.txt").readlines()  #scieżka bezwzględna gdzie u mnie plik ten występuje

        return tekst

    except Exception as e:  #dodanie jakiej kolwiek informacji o braku pliku
        
        blad = ("Błąd pliku.",e)

        return blad

#do poprawy, wyszukiwanie nie całości a części ciągu znaków
def wyszukaj(im,nr,list):

    l = len(list)
    n = []
    t = ("im"+"\t"+"nr")

    for i in range(l):
        if list[i] == t:
            n.append(i)

    return n

def zapis(tekst):   #\n dodać
    try:
        plik = open("lista.txt","a")
        plik.writelines(tekst)
        plik.close()

        t = "Dopisano pomyślnie"   #trzeba zrobić warynek żeby nie można było woisać jako nr. telefonu dowolnego znaku..

        return t

    except Exception as e:

        return e

def kasowanie(list):
    
    l = len(list)
    for i in range(l):
        print(i+1,list[i])

    n = int(input("Podaj numer linii do usunięcia: "))

    os.system('cls')   #czyszczenie konsoli

    t = list.pop(n-1)
    
    try:
        plik = open("lista.txt","w")
        plik.writelines(list)
        plik.close()
        print ("Skasowano.",t)

    except Exception as e:

        return e

while True:

    #os.system('cls')
    lista = odczyt()    #odczyt z pliku na samym początku aby reszta funkcji działała poprawnie a nie sypała błędami

    print("\nWybierz czynność, podając numer przy niej.\n"
          "1. Pokaż liste.\n"
          "2. Dopisz do listy.\n"
          "3. Usuń z listy.\n"
          "4. Wyszukaj daną osobę lub numer.\n"
          "5. Wyjście.\n")

    try:
        w = int(input("Numer operacji do wykonania: "))

        if w  == 1:
            
            for i in lista:
                print(i)

        elif w == 2 :
            x = input(str('Wpisz imię: '))
            y = input(str('Wpisz numer telefonu: '))
            linia = str('\n'+x+'\t'+y) #skrócenie zapisu twojego Rafał
            zapis(linia)
            print('pomyślnie dopisano do listy')

        elif w == 3:
            kasowanie(lista)

        elif w == 5:
            input("Wciśnij dowolny klawisz aby zamknąć.")
            sys.exit(0)

        else:
            print("Podałeś za niewłaściwą liczbę.\nWpisz jeszcze raz.") 


    except Exception as e:
        print("Błąd:",e)

