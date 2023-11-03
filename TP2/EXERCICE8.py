L = [1, 2, 5, 8, 6, 2, 5, 9, 1, 8, 8]

nombre = int(input("Donner le nombre a chercher dans la liste : "))
index = []
occurrence = []
 
for i in range(len(L)):
    if L[i] == nombre:
        occurrence.append(L[i])
        index.append(i)
#print(occurrence)
#print(index)

if index:
    print(f"Le nombre d'occurrence de {nombre} est : {len(occurrence)}")
    print(f"Les index d'occurence : {index}")
else:
    print(f"Nombre {nombre} n'existe pas.")