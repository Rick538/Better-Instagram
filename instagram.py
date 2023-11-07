import instaloader
import time
import json
import re
from chatgpt_selenium_automation.handler.chatgpt_selenium_automation import ChatGPTAutomation
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

 
# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
 
#Loading a profile from an Instagram handle

##username = input("Enter your Instagram username: ")
profile = instaloader.Profile.from_username(bot.context, 'josef.jindra.666')


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
        print(formated)



chrome_driver_path = r"C:\chromedriver.exe"
chrome_path = r'"C:\Program Files\Google\Chrome\Application\chrome.exe"'
chatgpt = ChatGPTAutomation(chrome_path, chrome_driver_path)


with open('post_data.json', 'r', encoding='utf-8') as f:
    prompt = f.read()

question = "Tell me what should i change on my instagram profile to be a famous person, use this data for analysis:" + str(prompt)
chatgpt.send_prompt_to_chatgpt(question)
response = chatgpt.return_last_response()
print(response)

file_name = r"B:\conve\conversation.txt"
chatgpt.save_conversation(file_name)
print(file_name)

chatgpt.quit()