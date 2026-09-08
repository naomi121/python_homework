import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Task 6: Initialize Selenium Webdriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Task 6: Load OWASP Top 10 Page
url = "https://owasp.org/www-project-top-ten/"
driver.get(url)

time.sleep(3)

owasp_top_10 = []

# Task 6: Target the exact top 10 list elements via structural XPath
# Locates anchor tags inside the list items of the main project overview section
vulnerability_elements = driver.find_elements(
    By.XPATH, "//section[@id='sec-main']//ul/li/a[contains(@href, 'A0') or contains(@href, 'A10')]"
)

# Fallback XPath targeting article content list directly if DOM structure shifts
if not vulnerability_elements:
    vulnerability_elements = driver.find_elements(
        By.XPATH, "//article[contains(@class, 'page-content')]//ul/li/a"
    )

# Task 6: Accumulate exactly the first 10 entries as dictionaries
for elem in vulnerability_elements[:10]:
    title = elem.text.strip()
    href = elem.get_attribute("href")
    
    if title and href:
        owasp_top_10.append({
            "Vulnerability Title": title,
            "URL": href
        })

driver.quit()

# Task 6: Print list to verify structure and length
print(f"Extracted {len(owasp_top_10)} vulnerabilities:")
for item in owasp_top_10:
    print(item)

# Task 6: Save DataFrame to CSV
df = pd.DataFrame(owasp_top_10)
df.to_csv("owasp_top_10.csv", index=False)