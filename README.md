# Gestion de Stock avec SQLAlchemy (App CLI créée par Woody Belony)

Ce projet est une application Python permettant de gérer un système de stock, en utilisant SQLAlchemy pour l'accès à la base de données. Il inclut des modèles pour **Produits**, **Fournisseurs** et **Mouvements d'inventaire**.

---

## Fonctionnalités

- **Gestion des produits** : ajout, mise à jour, suppression
- **Gestion des fournisseurs** : ajout, mise à jour, suppression
- **Suivi des mouvements d'inventaire** : entrées et sorties
- **Utilisation d'une base de données relationnelle** via SQLAlchemy

---

## Prérequis

- Python 3.x
- SQLAlchemy

---

## Installation

1. **Cloner le dépôt**

```bash
git clone https://github.com/votre-utilisateur/votre-repo.git
cd votre-repo
```

2. **Créer un environnement virtuel (optionnel mais recommandé)**

```bash
python -m venv env
# Sur Linux/Mac
source env/bin/activate
# Sur Windows
.\env\Scripts\activate
```

3. **Installer les dépendances**

```bash
pip install sqlalchemy
```

---

## Configuration

Modifiez ou créez votre fichier `main.py` pour configurer la connexion à votre base de données. Voici un exemple avec SQLite :

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Connexion à la base de données SQLite
engine = create_engine('sqlite:///stock.db')

# Création des tables si elles n'existent pas
Base.metadata.create_all(engine)

# Création d'une session
Session = sessionmaker(bind=engine)
session = Session()

# Ajoutez votre logique ici
```

---

## Utilisation

Lancez votre script principal :

```bash
python main.py
```

Ajoutez votre logique pour manipuler la base de données (CRUD) selon vos besoins.

---

## Structure du projet

```
BestProjectPython/
├── main.py
├── models/
│   ├── __init__.py
│   ├── base.py
│   ├── product.py
│   ├── supplier.py
│   └── inventory_movement.py
└── README.md
```

---

## Contributions

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir des issues ou à proposer des pull requests.

---
