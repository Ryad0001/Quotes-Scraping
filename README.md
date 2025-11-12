# Quotes-Scraping 🌐


https://github.com/user-attachments/assets/e9877871-40e3-4921-bad2-cb5e49b4df31


## Description
This project scrapes quotes from the website `https://quotes.toscrape.com/` and stores the extracted data in a JSON file. A FastAPI service is then used to expose this data so it can be reused in other applications.

<img width="942" height="199" alt="image" src="https://github.com/user-attachments/assets/bd67412d-266c-411d-9aa5-63cfaea5d2f8" />


## Features
- Scrape quotes (text + author + tags)
- Store the result in `quotes.json`
- Provide a simple API using FastAPI

## Project Structure
```
Quotes-Scraping/
│
├── main.py                # Main script API
├── scrape_quotes.py       # Scraping script
├── quotes.json            # JSON file containing scraped quotes
├── requirements.txt       # List of dependencies
└── notebook.ipynb         # Notebook for exploration (if used)
```


## Installation
```bash
git clone https://github.com/Ryad0001/Quotes-Scraping.git
cd Quotes-Scraping
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate         # Windows
pip install -r requirements.txt 
```

If you do not have a `requirements.txt`, install manually:
```bash
pip install fastapi uvicorn requests beautifulsoup4
```

## Run the Scraper
```bash
python scrape_quotes.py
```
This will create or update the `quotes.json` file.

## Run the API
```bash
uvicorn main:app --reload --port 8001
```

API available at:
```
http://127.0.0.1:8001
```

<img width="941" height="264" alt="image" src="https://github.com/user-attachments/assets/6592c9ef-d2ab-41ab-bee1-d6b7de6ea399" />


## API Endpoints
| Method | Route | Description |
|--------|-------|-------------|
| GET    | `/` | Health check |
| GET    | `/items` | Returns all quotes |
| GET    | `/items/{id}` | Returns a specific quote by its ID |



### Example Response for `/items/2`
```json
{
 "id": 2,
    "Quote": "“It is our choices, Harry, that show what we truly are, far more than our abilities.”",
    "Author": "J.K. Rowling",
    "Tags": [
      "abilities",
      "choices"
}
```

## License
Free to use for educational purposes.
