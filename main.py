import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

product_info = []

for page in range(1, 311):
    driver.get(f'https://www.kickscrew.com/collections/nike?page={page}')
    list_atags = driver.find_elements(By.CLASS_NAME, 'hit')
    for index, tags in enumerate(list_atags):
        try:
            # Re-fetch the element before clicking
            tags = driver.find_elements(By.CLASS_NAME, 'hit')[index]
            tags.click()
            product_info.append(driver.find_elements(By.CLASS_NAME, 'pdp-product-info-col'))
        except StaleElementReferenceException:
            # Handle StaleElementException by refreshing the list of elements
            list_atags = driver.find_elements(By.CLASS_NAME, 'hit')
            tags = list_atags[index]  # Get the element again after refresh
            tags.click()
            product_info.append(driver.find_elements(By.CLASS_NAME, 'pdp-product-info-col'))

        driver.back()
        # Wait for the list of elements to be present again before proceeding
        WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'hit')))

driver.quit()