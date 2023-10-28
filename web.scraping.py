from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import pickle
from selenium import webdriver
import os.path

#Opening the firefox
firefox_options = Options()
options = Options()
##options.add_argument("-headless")
driver = webdriver.Firefox(options=options)
##print("headless inicialized")



#Creating the cookie
def Creating_Cookie():

    driver.get('https://www.instagram.com')

    #Entering the site
    try:
        time.sleep(5)
        click = driver.find_element(By.CSS_SELECTOR,'button._a9--:nth-child(2)')
        click.click()
        time.sleep(5)
    except Exception:
        print("Servers of instagram are down, please try again later")

    ##Logining to the instagram
    USERNAME = 'karlito_podel9'
    PASSWORD = 'AeeRhKK*27869'
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
    save_cookie(driver,'C:/tmp/cookie')

#Saving cookie
def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)
#Loading cookie
def load_cookie(driver, path):
     with open(path, 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
            driver.add_cookie(cookie)

#Checking if cookie is saved
check_file = os.path.exists('C:/tmp/cookie')
if not check_file:
    Creating_Cookie()
else:
    load_cookie(driver, 'C:/tmp/cookie')

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
    image_date = driver.find_element(By.CSS_SELECTOR,'._aaqe')
    time.sleep(5)
    print(image_date)
except:
    print("chyba")
time.sleep(50)
driver.quit()