from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Provide the path to your WebDriver here


url = "https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787"

# Setting up the WebDriver
# Provide the path to your WebDriver here
# webdriver_path = '/path/to/your/chromedriver'

driver = webdriver.Chrome()
driver.get(url)

try:
    # Wait for the table to load (adjust the time accordingly)
    table = driver.find_element(By.ID, "table_id")
    
    # Extract the headers
    headers = [th.text.strip() for th in table.find_elements(By.TAG_NAME, "th")]

    # Extract the first five rows of data
    rows = table.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr")[:5]
    
    for row in rows:
        row_data = [td.text.strip() for td in row.find_elements(By.TAG_NAME, "td")]
        combined_data = dict(zip(headers, row_data))
        print(combined_data)
except Exception as e:
    print("An error occurred:", e)
finally:
    driver.quit()
