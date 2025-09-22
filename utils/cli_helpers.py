def print_menu():
    print("\n--- Menu Inventaire ---")
    print("1. Ajouter un produit")
    print("2. Voir tous les produits")
    print("3. Ajouter un fournisseur")
    print("4. Voir tous les fournisseurs")
    print("5. Enregistrer un mouvement d'inventaire")
    print("q. Quitter")

def get_choice():
    return input("Votre choix: ").strip()