ageUtilisateur = input("Quel âge as tu ? : ")

try:
    ageUtilisateur = int(ageUtilisateur)
except:
    print("L'age indiqué est incorrect")
else:
    print(ageUtilisateur)
finally:
    print("Peut import ce qu'il se passe, j'affiche ce message car c'est un finally")

