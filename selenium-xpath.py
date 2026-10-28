from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Setup
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)

try:
    # Open the YouTube video (replace with your own URL)
    driver.get("https://www.youtube.com/watch?v=VIDEO_ID")

    # Wait for the Chapters chip to be clickable
    chapters_xpath = "//button[@role='tab' and @aria-label='Chapters']"
    chapters_btn = wait.until(EC.element_to_be_clickable((By.XPATH, chapters_xpath)))

    # Normal click
    chapters_btn.click()
    print("Clicked on Chapters button")

except TimeoutException:
    print("Chapters button not found or not clickable")

finally:
    driver.quit()