
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://quotes.toscrape.com/js-delayed/page/5/"

parts = URL.split('/')
URL_base = '/'.join(parts[:-2]) + '/'
page_number = int(parts[-2])

driver = webdriver.Chrome()
first_quote = None

try:
    previousElement = ""
    while previousElement is not None:
        url = URL_base + str(page_number)
        driver.get(url)
        previousElement = None
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "quote"))
        )
        page_content = driver.page_source
        soup = BeautifulSoup(page_content, "html.parser")
        # previous button
        previousElement = soup.find("li", class_="previous")
        # Extraire les citations
        quotes = soup.find_all("div", class_="quote")
        if len(quotes) > 0:
            quote = quotes[0]
            first_quote = {
                "text": quote.find("span", class_="text").text.strip(),
                "author": quote.find("small", class_="author").text.strip(),
                "tags": [tag.get_text() for tag in quote.find_all("a", class_="tag")]
            }
        page_number -= 1
finally:
    driver.close()
    print("La premier citation est :")
    print(f"Citation : {first_quote["text"]}")
    print(f"Auteur : {first_quote["author"]}")
    print(f"Tags : {first_quote["tags"]}")