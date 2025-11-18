import requests
from bs4 import BeautifulSoup

URL = 'https://www.bbc.com/news'
FILENAME = 'headlines.txt'

try:
    response = requests.get(URL)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = soup.find_all('h2')
    
    headline_list = []
    for headline in headlines:
        text = headline.get_text().strip()
        if text:
            headline_list.append(text)
            
    with open(FILENAME, 'w', encoding='utf-8') as f:
        for headline in headline_list:
            f.write(headline + '\n')
            
    print(f"Successfully scraped {len(headline_list)} headlines and saved them to {FILENAME}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")