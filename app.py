import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


client = MongoClient("mongodb://localhost:27017/")
db = client['nailib_datavalue']
collection = db['ia_samples']


def clean_text(text):
    """Clean and normalize text."""
    return text.strip() if text else "N/A"

def parse_page(url):
    """Scrape data from the given Nailib page."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        
        title = clean_text(soup.find('h1').get_text()) if soup.find('h1') else "N/A"

        
        subject = clean_text(soup.find('span', class_='subject').get_text()) if soup.find('span', class_='subject') else "N/A"

        
        description = clean_text(soup.find('div', class_='description').get_text()) if soup.find('div', class_='description') else "N/A"

        meta_info = soup.find('div', class_='meta-info').get_text() if soup.find('div', class_='meta-info') else "N/A"
        word_count = int(meta_info.split(' ')[0]) if meta_info != "N/A" and "words" in meta_info else 0
        read_time = meta_info.split('/')[-1].strip() if meta_info != "N/A" else "N/A"

        
        sections = {}
        for section in soup.find_all('div', class_='section'):
            section_title = clean_text(section.find('h2').get_text()) if section.find('h2') else "N/A"
            section_content = clean_text(section.get_text(separator="\n"))
            sections[section_title] = section_content

        
        file_link = soup.find('a', class_='download-link')['href'] if soup.find('a', class_='download-link') else "N/A"

        
        publication_date = clean_text(soup.find('time', class_='published-date').get_text()) if soup.find('time', class_='published-date') else "N/A"

        return {
            "title": title,
            "subject": subject,
            "description": description,
            "sections": sections,
            "word_count": word_count,
            "read_time": read_time,
            "file_link": file_link,
            "publication_date": publication_date
        }
    except Exception as e:
        logging.error(f"Error parsing page {url}: {e}")
        return None

def save_to_mongo(data):
    """Save scraped data to MongoDB."""
    try:
        collection.update_one({"title": data['title']}, {"$set": data}, upsert=True)
        logging.info(f"Data saved for: {data['title']}")
    except Exception as e:
        logging.error(f"Error saving to MongoDB: {e}")


def scrape_nailib():
    """Main function to scrape IA/EE samples and save to MongoDB."""
    base_urls = [
        "https://nailib.com/ee-sample",  
        "https://nailib.com/ib-flashcards"  
    ]
    
    for url in base_urls:
        logging.info(f"Scraping URL: {url}")
        data = parse_page(url)
        if data:
            save_to_mongo(data)

if __name__ == "__main__":
    scrape_nailib()
