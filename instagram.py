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
from selenium.webdriver.common.keys import Keys

 
# Creating an instance of the Instaloader class
def load_instagram():
    """Load data from instagram"""
    username = input("Enter your Instagram username: ")
    bot = instaloader.Instaloader()
    bot.load_session_from_file("karlito_podel9")
    profile_insta = instaloader.Profile.from_username(bot.context, username)
    print("Instagram profile")
    return profile_insta

#Opening the google browser
def Opening_Google():
    """Open the google browser with saved session"""
    options = Options()
    options.add_argument("user-data-dir=C:\selenium")
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(options)
    return driver

def clear_post_data():
    """Clear the json file named post_data"""
    with open('post_data.json', 'w', encoding='utf-8') as json_file:
        json_file.truncate()

def profile_data():
    """Takes data from instagram profile and save them into json.file"""
    clear_post_data()
    profile = load_instagram()
    print("Profile data")
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
            print_jason()

def print_jason():
    """This will formate data in json.file into readable text for chatgpt"""
    with open('post_data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        formated = re.sub(r'[{}"\[\],]','', json.dumps(data, indent=3))
        return formated

def Sending_prompt_to_chatgpt():
    """Send a data from instagram to the chatgpt for analytics of better performance"""
    driver = Opening_Google()
    data_for_chatgpt = str(print_jason())
    question = """Tell me what should i change on my instagram profile to make it better and get more attention from people, use this data for analysis:
    1) username: do you think that this username is good? or you think i should change it to make my profile look better"
    2) bio: do you think that this bio is good and creative or at least if it can tell what person im? 
    3) hastags: are those hastags that i have on my post good or should i try add newer?
    4) date: should i posted a more posts in short time or is this period good, like should i post every day or week
    5) caption: is the text of the caption good? or i should change it into something more informative, like info about the author or the post
    Please answer in the following questions and on the end of every question, and add some space at the end, please do not write the question, but only the point and the first word in which it is found and the answer, because it would be helpful and more readable
    """ + data_for_chatgpt
    print(question)
    time.sleep(5)
    driver.get("https://chat.openai.com")
    time.sleep(5)
    driver.find_element(By.ID,'prompt-textarea').click() 
    time.sleep(3)
    driver.find_element(By.ID,'prompt-textarea').send_keys(question)
    time.sleep(3)
    lines = data_for_chatgpt.splitlines()
    for line in lines:
        if line != '\n':
            driver.find_element(By.ID,'prompt-textarea').send_keys(line)
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,"button.absolute").click()
    time.sleep(3)
    Taking_response_data(driver)

def Taking_response_data(driver):
    """Takes data from chatgpt and prints it to the screen"""
    time.sleep(10)
    response_from_chatgpt = driver.find_element(By.CSS_SELECTOR,"#__next > div.relative.z-0.flex.h-full.w-full.overflow-hidden > div.relative.flex.h-full.max-w-full.flex-1.flex-col.overflow-hidden > main > div.flex.h-full.flex-col > div.flex-1.overflow-hidden > div > div > div > div.group.w-full.text-token-text-primary.border-b.border-black\/10.gizmo\:border-0.dark\:border-gray-900\/50.gizmo\:dark\:border-0.bg-gray-50.gizmo\:bg-transparent.dark\:bg-\[\#444654\].gizmo\:dark\:bg-transparent > div > div > div.relative.flex.w-\[calc\(100\%-50px\)\].flex-col.gizmo\:w-full.lg\:w-\[calc\(100\%-115px\)\].agent-turn > div > div.flex.flex-grow.flex-col.max-w-full.gap-3.gizmo\:gap-0 > div > div")
    time.sleep(5)
    response = open('response.txt', 'w')
    response.write(response_from_chatgpt)
    print(response.read())

def main():
    #Takes a list of data from instagram and write them into a json.file
    profile_data()
    Sending_prompt_to_chatgpt()
main()
   




