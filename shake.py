
e=3
c=3
f=4
g=4
a=5
h=5
b=6
d=6

figure=input("Y-a-t il une figure a l'intérieur de la forme?")
if figure == "oui":
    coast = float(input("Nombre de coté?"))
    if coast== f or coast == g:
        forme = input("La forme est elle rouge?")
        if forme == "oui":
            print ("La forme est G")
        else:
            print ("La forme est F")
    elif coast == a or coast == h:
        rouge = input("La forme est elle rouge?")
        if rouge == "oui":
            print ("La forme est H")
        else:
            print ("La forme est A")
else:
    coast=float(input("Nombre de coté?"))
    if coast == b or coast == d:
        forme = input("La forme est elle rouge?")
        if forme == "oui":
            print ("La forme est D")
        else:
            print ("La forme est B")
    elif coast == c or coast == e:
        rouge = input("La forme est elle rouge?")
        if rouge == "oui":
            print ("La forme est C")
        else:
            print ("La forme est E")