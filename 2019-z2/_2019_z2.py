import os   #cls do czyszczenia ekranu
import sys  #do użycia exit(0) w celu zakończeni programu

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def odczyt():

    try:
        tekst = []
        tekst = open("lista.txt").readlines()

        return tekst

    except Exception as e:  #dodanie jakiej kolwiek informacji o braku pliku
        
        blad = ("Błąd pliku.",e)

        return blad

#wyszukiwanie po imieniu lub numerze-pełnych
def wyszukaj(list):

    print("Opcje wyszukiwania:\n"
    "1. Wyszukaj po imieniu.\n"
    "2. Wyszukaj po numerze telefonu.\n")
    w = input("Numer wyboru: ")

    wyniki =[]

    if w == '1':

        imie = str(input("Podaj imie: "))

        for i in list:

            for j in range(len(i)):
               if i[j] == '\t':
                   wyniki.append(i)
                   break
               if i[j] != imie[j]:
                 break

    elif w == '2':

        numer = str(input("Podaj numer: "))

        for i in list:

            n = len(numer)

            for j in range(len(i),0,-1):
                if i[j-2] == '\t':
                    wyniki.append(i)
                    break
                if i[j-2] != numer[n-1]:
                    break
                n-=1
    else:
        print("Błędny znak lub niepasujący numer.")

    if len(wyniki) == 0:
        wyniki.append("Brak wyników wyszukiwania")

    print("\nWyszukania:")
    for i in wyniki:
        print(i)


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

    os.system('clear')   #czyszczenie konsoli

    t = list.pop(n-1)
    
    try:
        plik = open("lista.txt","w")
        plik.writelines(list)
        plik.close()
        print ("Skasowano.",t)

    except Exception as e:

        return e

while True:

    lista = odczyt()    #odczyt z pliku na samym początku aby reszta funkcji działała poprawnie a nie sypała błędami

    print("\nWybierz czynność, podając numer przy niej.\n"
          "1. Pokaż liste.\n"
          "2. Dopisz do listy.\n"
          "3. Usuń z listy.\n"
          "4. Wyszukaj daną osobę lub numer.\n"
          "5. Wyjście.\n")

    try:
        w = int(input("Numer operacji do wykonania: "))
        cls()
        if w  == 1:
            
            for i in lista:
                print(i)

        elif w == 2 :
            x = input(str('Wpisz imię: '))
            y = input(str('Wpisz numer telefonu: '))
            linia = str(x+'\t'+y+'\n') #skrócenie zapisu twojego Rafał
            zapis(linia)
            print('pomyślnie dopisano do listy')

        elif w == 3:
            kasowanie(lista)

        elif w == 4:    #dodano wyszukiwanie
            wyszukaj(lista)

        elif w == 5:
            input("Wciśnij dowolny klawisz aby zamknąć.")
            sys.exit(0)

        else:
            print("Podałeś za niewłaściwą liczbę.\nWpisz jeszcze raz.") 


    except Exception as e:
        print("Błąd:",e)

