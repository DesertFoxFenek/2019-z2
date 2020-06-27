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

    input("Wciśnij dowolny klawisz aby przejść dalej.")
    cls()


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

    cls()

    t = list.pop(n-1)
    
    try:
        plik = open("lista.txt","w")
        plik.writelines(list)
        plik.close()
        print ("Skasowano.",t)

        input("\nWciśnij dowolny klawisz aby wrócić do wyboru opcji.")
        cls()

    except Exception as e:

        return e

while True:

    lista = odczyt()    #odczyt z pliku na samym początku aby reszta funkcji działała poprawnie a nie sypała błędami

    print("Program ma na celu zarządzanie listą osób z ich numerami.\n"
          "Umożliwia on zobaczenie całej listy, dopisanie lub usunięcie rekordu oraz wyszukiwanie po imieniu lub numerze.\n"
          "\nWybierz czynność, podając numer przy niej.\n\a"
          "1. Pokaż liste.\n"
          "2. Dopisz do listy.\n"
          "3. Usuń z listy.\n"
          "4. Wyszukaj daną osobę lub numer.\n"
          "5. Wyjście.\n"
          "6. Autorzy, informacje o programie i środowisku tworzenia.\n")

    try:
        w = int(input("Numer operacji do wykonania: "))
        cls()
        if w  == 1:
            
            for i in lista:
                print(i)

            input("Wciśnij dowolny klawisz aby zamknąć.")
            cls()

        elif w == 2 :
            im = input(str('Wpisz imię: '))
            nr = input(str('Wpisz numer telefonu: '))
            linia = str(im+'\t'+nr+'\n') #skrócenie zapisu twojego Rafał
            zapis(linia)
            print('pomyślnie dopisano do listy')

        elif w == 3:
            kasowanie(lista)

        elif w == 4:    #dodano wyszukiwanie
            wyszukaj(lista)

        elif w == 5:
            input("Wciśnij dowolny klawisz aby zakończyć działanie programu.")
            sys.exit(0)

        elif w == 6:
            print("Autorzy: \n"
                  "Pomysł i projekt wstępny:                Dominik Lisiecki oraz Rafał Kęszycki\n"
                  "Kod:                                     Dominik Lisiecki oraz Rafał Kęszycki\n"
                  "Korekty kodu oraz kontrola błędów:       Dominik Lisiecki oraz Rafał Kęszycki\n"
                  "Testy pełne:                             Dominik Lisiecki oraz Rafał Kęszycki\n"
                  "Testy jednostkowe:                       Dominik Lisiecki\n"
                  "Pomysł na opis programu PDF:             Rafał Kęszycki\n"
                  "Opis programu:                           Dominik Lisiecki oraz Rafał Kęszycki\n"
                  "Znane błędy: \n"
                  "Wyszukiwanie pozwala na zdublowanie ostatniego wyrazu, a i tak znajdzie\nrekord, który miał by być normalnie bez literówki.\n\n"
                  "Środowisko użytkownika: \n"
                  "System operacyjny-główny:                Microsoft Windows 10 Pro 19041.329\n"
                  "System pomocniczy do testów:             Ubuntu 20.04\n"
                  "Usługa maszyny wirtualnej:               Microsoft Hyper-V 10.0.19041.1\n"
                  "Środowisko programistyczne:              Microsoft Visual Studio Community 2019 16.0.1 oraz 16.0.2\n"
                  "Język programowania:                     Python v3.7 (64-bit)\n\n")
            input("Wciśnij dowolny klawisz aby przejść do menu wyboru.")
            cls()

        else:
            print("Podałeś za niewłaściwą liczbę.\nWpisz jeszcze raz.") 


    except Exception as e:
        print("Błąd:",e)