def transformation_miroir(liste):
    # return liste[::-1]
    taille = len(liste)
    miroir = []
    for i in range(taille - 1, -1, -1):
        miroir.append(liste[i])
    return miroir

# Test
L = [8, 24, 48, 2, 16]
resultat = transformation_miroir(L)
print(resultat)
