import tkinter as tk
# Afficher les tâches
# Ajouter une tâche
# Supprimer une tâche
# Modifier une tâche
# Compléter une tâche
# Quitter

taches = []

def afficher_taches():
    fenetre_affichage = tk.Tk()
    fenetre_affichage.title("Liste de tâches")

    label_titre = tk.Label(fenetre_affichage, text="Ma liste de tâches")
    label_titre.pack()

    if not taches:
        label_vide = tk.Label(fenetre_affichage, text="Aucune tâche trouvée.")
        label_vide.pack()
    else:
        for tache in taches:
            label_tache = tk.Label(fenetre_affichage, text=f"- {tache}")
            label_tache.pack()

    bouton_fermer = tk.Button(fenetre_affichage, text="Fermer", command=fenetre_affichage.destroy)
    bouton_fermer.pack()

    fenetre_affichage.mainloop()


def ajouter_tache(nouvelle_tache):
    taches.append(nouvelle_tache)
    print(f'Tâche "{nouvelle_tache}" ajoutée.')


def supprimer_tache():
    afficher_taches()
    if not taches:
        print("Aucune tâche trouvée.")
        return None
    try:
        choix_supp = int(
            input("Entrez le numéro de la tâche à supprimer : ")) - 1
        if 0 <= choix_supp < len(taches):
            tache_supprimee = taches.pop(choix_supp)
            print(f'La tâche "{tache_supprimee}" a été supprimée avec succès.')
            return choix_supp
        else:
            print("Index de tâche invalide. Veuillez réessayer.")
            return None
    except ValueError:
        print("Veuillez entrer un numéro valide.")
        return None


def modifier_tache():
    while True:
        afficher_taches()
        if not taches:
            print("Aucune tâche trouvée.")
            return

        try:
            index = int(input("Entrez le numéro de la tâche à modifier : ")) - 1
            if 0 <= index < len(taches):
                nouvelle_tache = input("Entrez la nouvelle version de cette tâche : ")
                taches[index] = nouvelle_tache
                print("Votre tâche a été modifiée avec succès.")
            else:
                print("Index de tâche invalide. Veuillez réessayer.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")

        continuer_modification = input("Voulez-vous modifier une autre tâche ? (O/N) ").upper()
        if continuer_modification != 'O':
            break  

def completer_tache():
    afficher_taches() 
    if not taches:
        print("Aucune tâche trouvée.")
        return None  
    try:
        choix_complete = int(input("Veuillez saisir le numéro de la tâche que vous avez complétée : ")) - 1
        if 0 <= choix_complete < len(taches):
            tache_completee = taches.pop(choix_complete)
            print(f'La tâche "{tache_completee}" a été complétée avec succès.')
            return choix_complete
        else:
            print("Index de tâche invalide. Veuillez réessayer.")
            return None 
    except ValueError:
        print("Veuillez entrer un numéro valide.")
        return None
    





def main():
    while True:
        print("   ")
        print("**********")
        print(" ")
        print("1. Afficher les tâches")
        print(" ")
        print("2. Ajouter une tâche")
        print(" ")
        print("3. Supprimer une tâche")
        print(" ")
        print("4. Modifier une tâche")
        print(" ")
        print("5. Compléter une tâche")
        print(" ")
        print("6. Quitter")
        print(" ")

        choix = input(
            "Que voulez vous faire ? Choisissez un chiffre entre 1 et 6 : ")

        if choix == '1':
            z = "fji"
            while z !="z":
                afficher_taches()
                z = input("Appuyer sur z pour sortir : ")

        elif choix == '2':
            nouvelle_tache = input(
                "Entrez la tâche que vous souhaitez ajouter : ")
            ajouter_tache(nouvelle_tache)
        elif choix == '3':
            supprimer_tache()
        elif choix == '4':
            modifier_tache()
        elif choix == '5':
            completer_tache()
        elif choix == '6':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez saisir un chiffre entre 1 et 6 :")


if __name__ == "__main__":
    main()
