import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://owasp.org/www-project-top-ten/"
driver.get(url)

time.sleep(3)

owasp_top_10 = []

vulnerabilities = driver.find_elements(By.XPATH, "//a[contains(@href, 'A0') or contains(@href, 'A10')]")

seen_titles = set()

for vuln in vulnerabilities:
    title = vuln.text.strip()
    href = vuln.get_attribute("href")
    
    if title and title not in seen_titles and ("A0" in title or "A10" in title or "A0" in href):
        seen_titles.add(title)
        owasp_top_10.append({
            "Vulnerability Title": title,
            "URL": href
        })

driver.quit()

print(owasp_top_10)

df = pd.DataFrame(owasp_top_10)
df.to_csv("owasp_top_10.csv", index=False)


###