import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_page_data(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    title = driver.title
    body_text = driver.find_element(By.TAG_NAME, "body").text

    links = driver.find_elements(By.TAG_NAME, "a")
    url_list = []

    for link in links:
        href = link.get_attribute("href")
        if href:
            url_list.append(href)

    driver.quit()
    return title, body_text, url_list


def main():
    if len(sys.argv) != 2:
        print("Usage: python beautiful.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    print("\nProcessing...\n")

    title, body, links = get_page_data(url)

    print("TITLE:")
    print(title)

    print("\nBODY:")
    print(body)

    print("\nLINKS:")
    for link in links:
        print(link)


if __name__ == "__main__":
    main()
