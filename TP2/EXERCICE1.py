chiffre = input("Entrer un nombre entier : ")
nombre = int(chiffre) + int(chiffre * 2) + int(chiffre* 3) + int(chiffre * 4)
print(nombre)


"""
somme = 0
for i in range(1,5):
    nombre = int(str(chiffre) * i)
    somme = somme + nombre
print(f"La somme de {chiffre} + {chiffre * 11} + {chiffre * 111} + {chiffre * 1111} est égale à {somme}")
"""

nbr = int(input("Entrer un nombre entier :"))

nombre = nbr + nbr * 11 + nbr * 111 + nbr * 1111
print(nombre)
