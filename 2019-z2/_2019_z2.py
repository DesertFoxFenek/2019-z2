import subprocess   #cls do czyszczenia ekranu

def odczyt():

    try:
        tekst = []
        tekst = open("lista.txt").readlines()  #scieżka bezwzględna gdzie u mnie plik ten występuje

        return tekst

    except Exception as e:
        
        return e

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

    subprocess.call("cls", shell = True)   #czyszczenie konsoli

    t = list.pop(n-1)
    
    try:
        plik = open("lista.txt","w")
        plik.writelines(list)
        plik.close()
        print ("Skasowano",t)

    except Exception as e:

        return e

while True:

    #subprocess.call("cls", shell = True)

    print("Wybierz czynność, podając numer przy niej.\n"
          "1. Pokaż liste.\n"
          "2. Dopisz do listy.\n"
          "3. Usuń z listy.\n"
          "4. Wyszukaj daną osobę lub numer")

    try:
        w = int(input("Numer operacji do wykonania: "))

        if w  == 1:
            lista = odczyt()
            for i in lista:
                print(i)

        #coś próbuje od tąd
        elif w == 2 :
            x = input(str('Wpisz imię: '))
            y = input(str('Wpisz numer telefonu: '))
            linia = str('\n'+x+'\t'+y) #skrócenie zapisu twojego Rafał
            zapis(linia)
            print('pomyślnie dopisano do listy')

             
        #do tąd 
        #NOWE!!!-nie trzeba poprawione


    except Exception as e:
        print("Błąd:",e)

