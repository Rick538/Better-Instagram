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
def login_into_chatgpt(USERNAME,PASSWORD,driver):
        """This will login into your account in chatgpt if you dont have cookies, and makes you cookies so u dont have to write an email, password every time"""
        login_button = driver.find_element(By.CSS_SELECTOR,'#__next > div.flex.min-h-full.w-screen.flex-col.sm\:supports-\[min-height\:100dvh\]\:min-h-\[100dvh\].md\:grid.md\:grid-cols-2.lg\:grid-cols-\[60\%_40\%\] > div.relative.flex.grow.flex-col.items-center.justify-between.bg-white.px-5.py-8.text-black.dark\:bg-black.dark\:text-white.sm\:rounded-t-\[30px\].md\:rounded-none.md\:px-6 > div.relative.flex.w-full.grow.flex-col.items-center.justify-center > div > div > button:nth-child(1)')
        login_button.click()
        time.sleep(3)
        email_chatgpt = driver.find_element(By.CSS_SELECTOR,'#username')
        time.sleep(3)
        email_chatgpt.send_keys(USERNAME)
        time.sleep(3)
        button = driver.find_element(By.CSS_SELECTOR,'body > div > main > section > div > div > div > div.c959f9ac9.cf7e26009 > div > form > div.c028ea628 > button')
        time.sleep(3)
        button.click()
        time.sleep(3)
        email_chatgpt = driver.find_element(By.CSS_SELECTOR,'#password')
        time.sleep(3)
        email_chatgpt.send_keys(PASSWORD)
        time.sleep(3)
        button = driver.find_element(By.CSS_SELECTOR,'body > div.oai-wrapper > main > section > div > div > div > form > div.c028ea628 > button')
        time.sleep(3)
        button.click()
        time.sleep(3)

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