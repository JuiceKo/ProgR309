ageUtilisateur = input("Quel âge as tu ? : ")

try:
    ageUtilisateur = int(ageUtilisateur)
except:
    print("L'age indiqué est incorrect")
else:
    print(ageUtilisateur)
finally:
    print("Peut import ce qu'il se passe, j'affiche ce message car c'est un finally")
    
    
    if __name__ == "main":
    try:
        with open ("textfile.txt", "r") as f:
            for i in f:
                l= l.rstrip("\n\r")
                print(l)
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("You don't have permission to read this file")
    except FileExistsError:
        print("File already exists")
    except IOError:
        print("File not found") 
    else:
        print("main")
    finally:
        with open ("textefile.txt", "r") as f:
            for i in f:
                l= l.rstrip("\n\r")
                print(l)

