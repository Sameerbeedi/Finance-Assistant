# data_ingestion/filings_scraper.py
import requests

def scrape_filings(url=None):
    try:
        # CNBC API for earnings articles
        api_url = "https://www.cnbc.com/id/10001147/device/rss/rss.html"
        response = requests.get(api_url, headers={"User-Agent": "Mozilla/5.0"})

        if response.status_code != 200:
            print(f"Failed to fetch: {response.status_code}")
            return []

        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.content, "xml")
        items = soup.find_all("item")
        headlines = [item.title.text.strip() for item in items]
        return headlines[:5]
    except Exception as e:
        print(f"Scraping failed: {e}")
        return []
