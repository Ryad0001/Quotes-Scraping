import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

def scrape_quotes():
    data = []
    page = 1

    while True:
        url = f"https://quotes.toscrape.com/page/{page}/"
        html = urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")

        # Récupérer toutes les citations sur la page
        quotes = soup.find_all("div", class_="quote")

        # Si aucune citation => fin du site => on stoppe la boucle
        if len(quotes) == 0:
            break

        for q in quotes:
            text = q.find("span", class_="text").text.strip()
            author = q.find("small", class_="author").text.strip()
            tags = [tag.text for tag in q.find_all('a', class_='tag')]
            data.append([text, author, tags])

        page += 1  # page suivante

    # Convertir en DataFrame
    df = pd.DataFrame(data, columns=["Quote", "Author", "Tags"])

    # Ajouter un ID unique
    df['id'] = range(1, len(df) + 1)

    # Réordonner les colonnes
    df = df[['id', 'Quote', 'Author', 'Tags']]

    # Exporter en JSON
    df.to_json("quotes.json", orient="records", force_ascii=False)

    print(f"✅ Scraping terminé ! {len(df)} citations enregistrées dans quotes.json")

if __name__ == "__main__":
    scrape_quotes()
