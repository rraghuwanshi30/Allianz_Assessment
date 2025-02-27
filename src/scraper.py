from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from typing import List

BASE_URL = "https://www.scrapethissite.com/pages/forms/"

def fetch_html(page: int) -> str:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--ignore-certificate-errors")  # ✅ Bypass SSL
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--headless")  # Headless Mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.get(BASE_URL)

    print(f"🔍 Fetching Page {page}")

    if page > 1:
        try:
            pagination = driver.find_element(By.LINK_TEXT, str(page))
            pagination.click()
            time.sleep(3)
        except Exception as e:
            print(f"Page {page} not found: {e}")

    html = driver.page_source
    driver.quit()
    return html

def scrape_hockey_data() -> List[str]:
    html_pages = []
    first_page = fetch_html(1)
    soup = BeautifulSoup(first_page, 'html.parser')
    pagination = soup.select("ul.pagination li a")
    total_pages = len(pagination) if pagination else 1

    print(f"📄 Total Pages Found: {total_pages}")

    html_pages.append(first_page)

    for page in range(2, total_pages + 1):
        html_pages.append(fetch_html(page))

    return html_pages

if __name__ == "__main__":
    scrape_hockey_data()
