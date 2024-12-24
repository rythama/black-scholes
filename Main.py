# Importing selenium and statistical model
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import scipy
import datetime
import time

yahoo_url = "https://finance.yahoo.com/?guccounter=1"
gov_url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202412"

# Web scrape for vars
def scrape_current_price(product):
    driver = webdriver.Chrome()

    driver.get(yahoo_url)

    search_bar = driver.find_element(By.ID, "ybar-sbq")

    print("found search bar")

    search_bar.send_keys(product)
    search_bar.send_keys(Keys.RETURN)

    price_element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'Price')]"))
    )   

    price = price_element.text
    print(f"Current stock price: {price}")

    # 4. Quit WebDriver
    driver.quit()

    return price

# Calculate P and C
product = input("Enter Stock, Index, or ETF for analysis: ")
scrape_current_price(product)


# Return vars