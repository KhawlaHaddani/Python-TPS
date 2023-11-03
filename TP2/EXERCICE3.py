import random

nbr_diviner = random.randint(1,100)
essaie = 0
nbr_essaie = 7

print("On va jouer a un petit jeu, je vais générer un nombre entre 1 et 100 et tu va le devinez en 7 essaie")
while(nbr_essaie > 0):
    supposition = int(input(""))
    essaie += essaie
    if( supposition < 1 or supposition > 100):
        print("Oups, vous avez saisie un nombre en dehors de l'intervalle")
    elif( supposition < nbr_diviner):
        print("Oups, entrer un nombre plus grand !")
    elif( supposition > nbr_diviner):
        print("Oups, entrer un nombre plus petit !")
    else:
        print(f"Bravo {nbr_diviner} est le nombre que que j'ai choisit , vous l'avez deviner en {essaie} essaie")
        break
    nbr_essaie -= 1

if(essaie == 0):
    print(f"J'ai gagné , je suis le meilleur, le nombre que j'ai diviné est {nbr_diviner} Au revoir !")



