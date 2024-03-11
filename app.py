import tkinter as tk

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


def ajouter_tache():
    nouvelle_tache = saisie_tache.get()
    if nouvelle_tache:
        taches.append(nouvelle_tache)
        liste_taches.insert(tk.END, nouvelle_tache)
        saisie_tache.delete(0, tk.END)
        print(f'Tâche "{nouvelle_tache}" ajoutée.')
    else:
        print("Veuillez entrer une tâche valide.")

def supprimer_tache():
    index_selection = liste_taches.curselection()
    if index_selection:
        index = index_selection[0]
        tache_supprimee = taches.pop(index)
        liste_taches.delete(index)
        print(f'La tâche "{tache_supprimee}" a été supprimée avec succès.')
    else:
        print("Veuillez sélectionner une tâche à supprimer.")

def modifier_tache():
    index_selection = liste_taches.curselection()
    if index_selection:
        index = index_selection[0]
        ancienne_tache = liste_taches.get(index)
        nouvelle_tache = saisie_tache.get()
        if nouvelle_tache:
            taches[index] = nouvelle_tache
            liste_taches.delete(index)
            liste_taches.insert(index, nouvelle_tache)
            saisie_tache.delete(0, tk.END)
            print(f'La tâche "{ancienne_tache}" a été modifiée avec succès.')
        else:
            print("Veuillez entrer une tâche valide.")
    else:
        print("Veuillez sélectionner une tâche à modifier.")

def completer_tache():
    index_selection = liste_taches.curselection()
    if index_selection:
        index = index_selection[0]
        tache_completee = taches.pop(index)
        liste_taches.delete(index)
        print(f'La tâche "{tache_completee}" a été complétée avec succès.')
    else:
        print("Veuillez sélectionner une tâche à compléter.")

def main():
    fenetre_principale = tk.Tk()
    fenetre_principale.title("Gestionnaire de tâches")

    label_tache = tk.Label(fenetre_principale, text="Tâche :")
    label_tache.pack()

    saisie_tache = tk.Entry(fenetre_principale)
    saisie_tache.pack()

    bouton_ajouter = tk.Button(fenetre_principale, text="Ajouter", command=ajouter_tache)
    bouton_ajouter.pack()

    liste_taches = tk.Listbox(fenetre_principale)
    liste_taches.pack()

    bouton_supprimer = tk.Button(fenetre_principale, text="Supprimer", command=supprimer_tache)
    bouton_supprimer.pack()

    bouton_modifier = tk.Button(fenetre_principale, text="Modifier", command=modifier_tache)
    bouton_modifier.pack()

    bouton_completer = tk.Button(fenetre_principale, text="Compléter", command=completer_tache)
    bouton_completer.pack()

    bouton_afficher = tk.Button(fenetre_principale, text="Afficher", command=afficher_taches)
    bouton_afficher.pack()

    bouton_quitter = tk.Button(fenetre_principale, text="Quitter", command=fenetre_principale.quit)
    bouton_quitter.pack()

    fenetre_principale.mainloop()

if __name__ == "__main__":
    main()
