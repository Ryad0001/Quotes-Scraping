from fastapi import FastAPI
import json

app = FastAPI()

# Charger le fichier JSON au démarrage
with open("quotes.json", "r", encoding="utf-8") as f:
    data = json.load(f)


@app.get("/")
def root_test():
    return {"message": "API OK"}


@app.get("/items")
def get_all_quotes():
    return data


@app.get("/items/{item_id}")
def quote_from_id(item_id: int):
    for item in data:
        if item["id"] == item_id:
            return item
    return {"error": "Item non trouvé"}

