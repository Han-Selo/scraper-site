from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def scraper(keywords):
    url = f'https://www.br.de/nachrichten/suche?param={keywords}'

    chrome_options = Options()
    chrome_options.add_argument('--headless')

    # Start a new Selenium WebDriver (make sure you have ChromeDriver installed)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    # Wait for the page to load (you may need to adjust the sleep duration)
    time.sleep(1)

    # Get the page source after dynamic content is loaded
    page_source = driver.page_source

    # Parse the HTML content
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find all <a> tags with the specified class
    target_class = 'aitl-gtm ArticleItemResultsItem_link__BxItm'
    article_links = soup.find_all('a', class_=target_class)

    # Extract href attributes from the <a> tags
    hrefs = ["https://www.br.de" + a.get('href') for a in article_links]

    # Close the browser
    driver.quit()

    return hrefs