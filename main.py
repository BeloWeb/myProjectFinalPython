import sys
from models import Base, Product, Supplier, InventoryMovement
from database.session import engine, get_session
from utils.cli_helpers import print_menu, get_choice
from models.category import Category
from models.supplier import Supplier
from models.item import Item

def initialize_db():
    Base.metadata.create_all(bind=engine)

def main():
    initialize_db()
    session = get_session()

    while True:
        print_menu()
        choice = get_choice()

        if choice == '1':
            # Ajouter un produit
            name = input("Nom du produit: ")
            description = input("Description: ")
            price = float(input("Prix: "))
            product = Product(name=name, description=description, price=price)
            session.add(product)
            session.commit()
            print("Produit ajouté.")
        elif choice == '2':
            # Voir tous les produits
            products = session.query(Product).all()
            for p in products:
                print(p)
        elif choice == '3':
            # Ajouter un fournisseur
            name = input("Nom du fournisseur: ")
            contact = input("Contact: ")
            supplier = Supplier(name=name, contact_info=contact)
            session.add(supplier)
            session.commit()
            print("Fournisseur ajouté.")
        elif choice == '4':
            # Voir tous les fournisseurs
            suppliers = session.query(Supplier).all()
            for s in suppliers:
                print(s)
        elif choice == '5':
            # Enregistrer un mouvement d'inventaire
            product_id = int(input("ID du produit: "))
            quantity_change = int(input("Quantité (positive pour entrée, négative pour sortie): "))
            movement_type = 'entry' if quantity_change > 0 else 'exit'
            movement = InventoryMovement(product_id=product_id, quantity_change=quantity_change, movement_type=movement_type)
            session.add(movement)
            # Modifier la quantité du produit
            product = session.query(Product).get(product_id)
            if product:
                product.quantity += quantity_change
                session.commit()
                print("Mouvement enregistré et stock mis à jour.")
            else:
                print("Produit non trouvé.")
        elif choice.lower() == 'q':
            print("Au revoir!")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()