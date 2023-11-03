numbers = input("Entrez une liste d'entiers séparés par des espaces : ").split()

number_to_remove = input("Entrez le nombre que vous souhaitez supprimer : ")

nouveau_list = []

for num in numbers:
    if num != number_to_remove:
        nouveau_list.append(num)

print("Liste mise à jour :", nouveau_list)