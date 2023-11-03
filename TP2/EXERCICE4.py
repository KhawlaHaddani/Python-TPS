# en utilisant deux listes intermediaire
L = [1, -30, 0, -2, 500, 4, 2, 100]
negatifs = []
positifs = []

for nbr in L:
    if nbr < 0:
        negatifs.append(nbr)
    else:
        positifs.append(nbr)
        
M = negatifs + positifs
print(M)


# en utilise la liste M directement 
L = [1, -30, 0, -2, 500, 4, 2, 100]
M = []
for nombre in L:
    if nombre < 0:
        M.append(nombre)
for nombre in L:
    if nombre >= 0:
        M.append(nombre)

print(M)





