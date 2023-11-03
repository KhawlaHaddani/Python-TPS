def insert_in_list(L, val):
    for i in range(len(L)):
        if L[i] > val:
            L.insert(i, val)
            return

    # Si val est plus grand que tous les éléments dans la liste, l'ajouter à la fin
    L.append(val)
    
L = [1, 3, 5, 7, 9]
nbr = int(input("Donner le nombre a inserer : "))
insert_in_list(L, nbr)
print(L)  


