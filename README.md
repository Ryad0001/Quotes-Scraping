# Quotes-Scraping

## Description
This project scrapes quotes from the website `https://quotes.toscrape.com/` and stores the extracted data in a JSON file. A FastAPI service is then used to expose this data so it can be reused in other applications.

## Features
- Scrape quotes (text + author)
- Store the result in `quotes.json`
- Provide a simple API using FastAPI

## Project Structure
```
Quotes-Scraping/
│
├── main.py                # Main script (scraping + API)
├── quotes.json            # JSON file containing scraped quotes
├── requirements.txt       # List of dependencies (optional if present)
└── notebook.ipynb         # Notebook for exploration (if used)
```

## Requirements
- Python 3.8+
- pip installed

## Installation
```bash
git clone https://github.com/Ryad0001/Quotes-Scraping.git
cd Quotes-Scraping
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate         # Windows
pip install -r requirements.txt # if this file exists
```

If you do not have a `requirements.txt`, install manually:
```bash
pip install fastapi uvicorn requests beautifulsoup4
```

## Run the Scraper
```bash
python main.py
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
  "quote": "Life is beautiful.",
  "author": "Sample Author"
}
```

## Contribution
Contributions are welcome.  
Workflow:
```
fork → create branch → commit changes → open pull request
```

## License
Free to use for educational purposes.
