def main():
    print("Bienvenue dans le programme de calcul !")
    
    while True:
        try:
            a = int(input("Entrez le premier nombre : "))
            b = int(input("Entrez le deuxième nombre : "))
        except ValueError:
            print("Veuillez entrer des nombres valides.")
            continue

        operation = input("Choisissez l'opération (somme, produit, différence) : ").lower()

        if operation == "somme":
            print(f"La somme de {a} et {b} est {a + b}.")
        elif operation == "produit":
            print(f"Le produit de {a} et {b} est {a * b}.")
        elif operation == "différence":
            print(f"La différence entre {a} et {b} est {a - b}.")
        else:
            print("Opération non reconnue. Essayez encore.")
            continue
        
        print("Calcul effectué avec succès et opération terminée !")
        print("Calcul effectué avec succès !")  # Garder les deux messages
        
        continuer = input("Souhaitez-vous faire un autre calcul ? (oui/non) : ").lower()
        if continuer != "oui":
            print("Merci d'avoir utilisé le programme de calcul. À bientôt !")
            break

def produit(a, b):
    print(f"Le produit de {a} et {b} est {a * b}.")

def difference(a, b):
    return a - b

if __name__ == "__main__":
    main()
