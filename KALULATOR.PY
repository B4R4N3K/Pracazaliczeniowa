print("WYŚMIENITY KALKULATOR \n")

a =int(input("podaj pierwszą cyfrę:"))
b =int(input("podaj drugą cyfrę:"))
c = input("Jaką czynność matematyczmną chcesz wykonac (+, -, *, /):")

operator = {"+":a+b,"-":a-b,"*":a*b,"/":a/b}

if c == "+":
    print(operator["+"])
elif c == "-":
    print(operator["-"])
elif c == "*":
    print(operator["*"])
elif c == "/":
    print(operator["/"])
else :
    print("Błąd nieobsługiwany operator")
