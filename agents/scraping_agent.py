# agents/scraping_agent.py
import requests
from bs4 import BeautifulSoup

def scrape_earnings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.text  # placeholder
