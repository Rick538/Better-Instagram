import instaloader
import time
import json
import re
from selenium.webdriver.common.by import By
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from secret import USERNAME, PASSWORD


 
# Creating an instance of the Instaloader class
#username = input("Enter your Instagram username: ")
def load_session_from_file():
    bot = instaloader.Instaloader()
    bot.load_session_from_file("karlito_podel9")
    #Loading a profile from an Instagram handle

    profile = instaloader.Profile.from_username(bot.context, 'josef.jindra.666')


#Opening the google browser
options = Options()
options.add_argument("user-data-dir=C:\selenium")
options.binary_location = r"C:\Program Files\Google\Chrome Beta\Application\chrome.exe"
driver = webdriver.Chrome(options)

def post_data():
    about_user = {
        "Username: ": profile.username,
        "Number of Posts: ": profile.mediacount,
        "Following Count: ": profile.followees,
        "Bio: ": profile.biography,
        "External URL: ": profile.external_url
    }
    post_number = 0
    post_data_list = []
    post_data_list.append(about_user)
    for post in profile.get_posts():
        post_number += 1
        if post_number <= 10:
            time.sleep(5)
            post_dict = {
                "Post_id: ": post_number,
                "Post date: ": str(post.date_local),
                "Post caption: ": post.caption,
                "Post likes count: ": post.likes,
                "Post comments count: ": post.comments,
                "Post location: ": post.location,
                "Post hashtags: ": post.caption_hashtags
            }
            post_data_list.append(post_dict)
        else:
            with open('post_data.json', 'w', encoding='utf-8') as json_file:
                json.dump(post_data_list, json_file, ensure_ascii=False,indent=3)

def print_jason():
    with open('post_data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        formated = re.sub(r'[{}"\[\],]','', json.dumps(data, indent=3))
        return formated
    
def Sending_prompt_to_chatgpt(question):

    driver.get("https://chat.openai.com")
    time.sleep(3)
    driver.find_element(By.ID,'prompt-textarea').send_keys(question)
    time.sleep(3)
    button_send = driver.find_element(By.CSS_SELECTOR,"button.absolute")
    time.sleep(3)
    button_send.click()

def Taking_response_data():
    time.sleep(15)
    response_from_chatgpt = driver.find_element(By.CSS_SELECTOR,"div.group:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)")
    time.sleep(5)
    return response_from_chatgpt.text


def login_into_chatgpt(USERNAME,PASSWORD):
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

question = "Tell me what should i change on my instagram profile to make it better and get more attention from people, use this data for analysis:" + print_jason()

#Takes a list of data from instagram and write them into a json.file
#post_data()

#This will print formated data from json.file
#print_jason()
#Sends data to chatgpt
Sending_prompt_to_chatgpt(question)
#Takes response data from chatgpt
Taking_response_data()