import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import logging
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'data', 'market_intel.db')
LOG_PATH = os.path.join(BASE_DIR, 'logs', 'pipeline.log')
RAW_DATA_PATH = os.path.join(BASE_DIR, 'data', 'raw')

os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
os.makedirs(RAW_DATA_PATH, exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def fetch_ma_news():
    url = "https://www.bing.com/news/search?q=mergers+and+acquisitions+private+equity"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        leads = []

        for card in soup.find_all('a', class_='title'):
            leads.append({
                "title": card.text,
                "url": card.get('href'),
                "source": "Bing News",
                "scraped_at": datetime.now().isoformat(),
                "status": "New"
            })

        if leads:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            csv_path = os.path.join(RAW_DATA_PATH, f"scrape_{timestamp}.csv")
            
            df = pd.DataFrame(leads)
            df.to_csv(csv_path, index=False)

            conn = sqlite3.connect(DB_PATH)
            df.to_sql('leads', conn, if_exists='append', index=False)
            conn.close()

            print(f"Success: {len(leads)} leads saved to CSV and SQLite DB.")
            logging.info(f"Loaded {len(leads)} rows to DB")
        else:
            print("Warning: No articles found.")
            logging.warning("No articles found.")

    except Exception as e:
        print(f"Error: {e}")
        logging.error(f"Extraction failed: {e}")

if __name__ == "__main__":
    fetch_ma_news()