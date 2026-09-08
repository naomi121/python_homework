import time
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
driver.get(url)

time.sleep(5)

results = []

book_items = driver.find_elements(By.XPATH, "//li[contains(@class, 'cp-search-result-item')]")

for item in book_items:
    try:
        title_elem = item.find_element(By.XPATH, ".//*[contains(@class, 'cp-title')]")
        title = title_elem.text.strip()
    except Exception:
        title = "N/A"

    try:
        author_elems = item.find_elements(By.XPATH, ".//a[contains(@class, 'author-link')]")
        authors = [a.text.strip() for a in author_elems if a.text.strip()]
        author = "; ".join(authors) if authors else "N/A"
    except Exception:
        author = "N/A"

    try:
        format_elem = item.find_element(By.XPATH, ".//div[contains(@class, 'cp-format-indicator')]//span")
        format_year = format_elem.text.strip()
    except Exception:
        format_year = "N/A"

    results.append({
        "Title": title,
        "Author": author,
        "Format-Year": format_year
    })

driver.quit()

df = pd.DataFrame(results)
print(df)

df.to_csv("get_books.csv", index=False)

with open("get_books.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4)