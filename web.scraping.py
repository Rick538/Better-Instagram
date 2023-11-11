from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import selenium.webdriver
import time
import pickle
import json
from secret import USERNAME, PASSWORD


#Opening the firefox
firefox_options = Options(r"C:/geckodriver.exe")
options = Options()
options.add_argument("-headless")
driver = webdriver.Firefox(options=options)
##print("headless inicialized")



#Loging to the instagram
def Login():

    driver.get('https://chat.openai.com')

    #Entering the site
    try:
        time.sleep(5)
        click = driver.find_element(By.CSS_SELECTOR,'button.relative:nth-child(1)')
        click.click()
        time.sleep(5)
    except Exception:
        print("Servers of chatgpt are down, please try again later")

    ##Logining to the instagram
    time.sleep(5)
    username_el = driver.find_element(By.NAME,'username')
    time.sleep(5)
    password_el = driver.find_element(By.NAME,'password')
    time.sleep(5)

    username_el.send_keys(USERNAME)
    time.sleep(5)
    password_el.send_keys(PASSWORD)
    time.sleep(5)
    submit_el = driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
    time.sleep(5)
    submit_el.click()

Login()

try:
    #Loading instagram web.profile
    time.sleep(5)
    driver.get('https://www.instagram.com/josef.jindra.666/')
    time.sleep(5)

    #Writing out BIO
    bio = driver.find_element(By.CSS_SELECTOR,'h1._aacl')
    time.sleep(5)
    print(bio.text)

    #Entering another web.site
    time.sleep(5)
    link_to_image = driver.find_element(By.CSS_SELECTOR,'div._ac7v:nth-child(1) > div:nth-child(1)').click()                          
    time.sleep(5)

    #Looking for date of image
    image_date = driver.find_element(By.CSS_SELECTOR,'.x1yxbuor')
    time.sleep(5)
    print(image_date)

    #Looking for Likes image
    time.sleep(5)
    likes = driver.find_element(By.CSS_SELECTOR,'div.x2lwn1j:nth-child(2) > span:nth-child(1) > a:nth-child(2) > span:nth-child(1) > span:nth-child(1)')
    time.sleep(5)
    print(likes)

except:
    print("chyba")
time.sleep(50)
driver.quit()