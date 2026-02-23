import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_page_data(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    title = driver.title

    body_element = driver.find_element(By.TAG_NAME, "body")
    body_text = body_element.text

    links = driver.find_elements(By.TAG_NAME, "a")
    url_list = []
    for link in links:
        href = link.get_attribute("href")
        if href:
            url_list.append(href)

    driver.quit()

def main():
    url1 = input("Enter URL 1: ").strip()
    url2 = input("Enter URL 2: ").strip()

    print("\nProcessing URL 1...\n")
    title1, body1, links1 = get_page_data(url1)

    print("TITLE:")
    print(title1)
    print("\nBODY:")
    print(body1)
    print("\nLINKS:")
    for link in links1:
        print(link)

    print("\nProcessing URL 2...\n")
    title2, body2, links2 = get_page_data(url2)

    print("TITLE:")
    print(title2)

    print("\nBODY:")
    print(body2)

    print("\nLINKS:")
    for link in links2:
        print(link)

    return title, body_text, url_list

if __name__ == "__main__":
    main()
