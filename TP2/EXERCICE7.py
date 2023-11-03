L = [1, 2, 5, 8, 6, 2, 5, 9, 1, 8, 8]
index = 0
while index < len(L):
    element = L[index]
    if L.count(element) > 1:
        L.pop(index)
    else:
        index += 1

print(L)

"""
en utilisant une autre list 
L = [1, 2, 5, 8, 6, 2, 5, 9, 1, 8, 8]
liste_distincte = []

for element in L:
    if element not in liste_distincte:
        liste_distincte.append(element)

L = liste_distincte  # Mettre à jour la liste L avec les éléments distincts

print(L)
"""