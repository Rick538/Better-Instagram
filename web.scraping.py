from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

firefox_options = Options()
options = Options()
options.add_argument("-headless")

driver = webdriver.Firefox(options=options)
print("headless inicialized")

driver.get('https://www.instagram.com/josef.jindra.666/')
try:
    time.sleep(5)
    click = driver.find_element(By.CSS_SELECTOR,'button._a9--:nth-child(2)')
    click.click()
    time.sleep(5)
except Exception:
    print("Servers of instagram are down, please try again later")
search = driver.find_element(By.CSS_SELECTOR,'h1._aacl')
print(search.text)
time.sleep(100)
driver.quit()