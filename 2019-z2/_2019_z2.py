def odczyt():

    try:
        tekst = []
        tekst = open("C:/Users/doman/Documents/Programy Komputerowe/2019-2/lista.txt").readlines()  #scieżka bezwzględna gdzie u mnie plik ten występuje

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

def zapis(tekst):
    try:
        plik = open("C:/Users/doman/Documents/Programy Komputerowe/2019-2/lista.txt","a")
        plik.writelines(tekst)
        plik.close()
        t = "Dopisano pomyślnie"

        return t

    except Exception as e:

        return e


def kasowanie(list):
    
    l = len(list)
    for i in range(l):
        print(i+1,list[i])

    n = int(input("Podaj numer linii do usunięcia: "))

    t = list.pop(n-1)
    
    try:
        plik = open("C:/Users/doman/Documents/Programy Komputerowe/2019-2/lista.txt","w")
        plik.writelines(list)
        plik.close()
        print ("Skasowano",t)

    except Exception as e:

        return e



'''
a = input(str("Imie: "))
b = input(str("Numer telefonu: "))
t = (a+"\t"+b)
print(zapis(t))
'''
