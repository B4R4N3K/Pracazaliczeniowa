print("FAJNY KALKULATOR \n")

a =int(input("Podaj pierwszą cyfrę: "))
b =int(input("Podaj drugą liczbę: "))
c = input("Jaką czynnośc matematyczną chcesz wykonać (+,-,*,/):")

operator = {"+":a+b,"-":a-b,"*":a*b,"/":a/b}

if c in operator:
    print(operator[c])
else :
    print("Błąd nieobsługiwany operator")

