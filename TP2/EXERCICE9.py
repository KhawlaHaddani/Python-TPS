while True:
    direction = input("Choisissez la direction de la conversion (euro en dirham: 'eTOm' ou dirham en euro: 'mTOe'): ")
    if direction in ['eTOm', 'mTOe']:
        break
    else:
        print("Veuillez entrer 'e2m' ou 'm2e'.")

montants_convertie = []
while True:
    nbr = float(input("Donner un nombre (la saisir d'un nombre negative va arreter)"))
    if nbr < 0:
        break
    if direction == "eTOm":
        montant_DH = nbr * 10.86
        montants_convertie.append(f"{nbr} EUR = {montant_DH} MAD")
    elif direction == "mTOe":
        montant_euro = nbr * 0.092
        montants_convertie.append(f"{nbr} MAD = {montant_DH} EUR")

if montants_convertie:
    for montant in montants_convertie:
        print(montant)
else:
    print("aucune valeur a convertir")