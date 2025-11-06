<img width="944" height="299" alt="image" src="https://github.com/user-attachments/assets/e0e88fd5-33f4-4669-ace9-1a73f29599c4" />

<img width="932" height="271" alt="image" src="https://github.com/user-attachments/assets/d6bd835b-5401-4e1f-8c48-b490d2a1bbc8" />

# Quotes-Scraping

## Description
Ce projet permet de scraper des citations depuis le site `https://quotes.toscrape.com/` et de stocker les données obtenues dans un fichier JSON. Une API FastAPI permet ensuite d'exposer ces données pour les réutiliser dans d'autres applications.

## Fonctionnalités
- Scraping des citations (auteur + texte)
- Stockage dans `quotes.json`
- API FastAPI pour consulter les citations

## Structure du projet
```
Quotes-Scraping/
│
├── main.py                # Script principal (scraping + API)
├── quotes.json            # Fichier JSON contenant les citations extraites
├── requirements.txt       # Liste des dépendances (optionnel si présent)
└── notebook.ipynb         # Notebook d'exploration (si utilisé)
```

## Prérequis
- Python 3.8+
- pip installé

## Installation
```bash
git clone https://github.com/Ryad0001/Quotes-Scraping.git
cd Quotes-Scraping
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate         # Windows
pip install -r requirements.txt # si présent
```

Si tu n'as pas de `requirements.txt`, installe manuellement :
```bash
pip install fastapi uvicorn requests beautifulsoup4
```

## Lancer le scraping
```bash
python main.py
```
Cela génère ou met à jour le fichier `quotes.json`.

## Lancer l'API
```bash
uvicorn main:app --reload --port 8001
```
L'API sera accessible à :
```
http://127.0.0.1:8001
```

## Endpoints API
| Méthode | URL | Description |
|--------|-----|-------------|
| GET    | `/` | Vérifie que l'API fonctionne |
| GET    | `/items` | Retourne toutes les citations |
| GET    | `/items/{id}` | Retourne une citation selon son identifiant |

## Exemple de réponse `/items/2`
```json
{
  "id": 2,
  "quote": "La vie est belle.",
  "author": "Auteur Exemple"
}
```

## Contribution
Les contributions sont les bienvenues. Pour contribuer :
```
fork → créer branche → commit → pull request
```

## Licence
Libre d'utilisation à des fins d'apprentissage.


