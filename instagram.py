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
import requests
from gpt4all import GPT4All
import sys

 
# Creating an instance of the Instaloader class
def load_instagram():
    """Load data from instagram"""
    username = input("Enter your Instagram username: ")
    bot = instaloader.Instaloader()
    bot.load_session_from_file("karlito_podel9")
    profile_insta = instaloader.Profile.from_username(bot.context, username)
    print("Instagram profile")
    return profile_insta

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
        "Username:": profile.username,
        "Number of Posts:": profile.mediacount,
        "Following Count:": profile.followees,
        "Bio:": profile.biography,
        "External URL:": profile.external_url
    }
    post_number = 0
    post_data_list = []
    post_data_list.append(about_user)
    for post in profile.get_posts():
        post_number += 1
        if post_number <= 5:
            time.sleep(5)
            post_dict = {
                "Post_id:": post_number,
                "Post date:": str(post.date),
                "Post caption:": post.caption,
                "Post likes count:": post.likes,
                "Post comments count:": post.comments,
                "Post location:": post.location,
                "Post hashtags:": post.caption_hashtags
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
        formated = re.sub(r'[:\[\]{}",]','', json.dumps(data, indent=3))
        return formated
def formated_data(formated):
    with open('formated_data.txt', 'w', encoding='utf-8') as file:
        file.write(formated)
    
def chat():
    import openai
    data_for_chatgpt = str(print_jason())
    question =  data_for_chatgpt + """
        Use data i sent you at the start of this message.

        Tell me what I should change on my Instagram profile to make it better, follow these points:
            1) username: do you think the username I'm using is creative and original, or should I change it?
            2) bio: is this bio original and if so why do you think so, if not then why and what should I change.
            3) hastags: are the hastags I have on my post good or should I change them, add new ones.
            4) date: should I post more in a short time or is this period good, should I post every day or week?
            5) headline: is the headline text good? or should I change it to something more informative, like information about the author or post, or where I am
            Please answer the following questions in order so that they make sense and are legible.
        And finally, write down examples of how it could be and compare it with the data I sent.
        Write only answers and in points so it would be easier to understand.
        """

    openai.api_base = "http://localhost:4891/v1"

    openai.api_key = "not needed for a local LLM"

    model = "mistral-7b-openorca.Q4_0.gguf"
    with open('formated_data.txt', 'r', encoding='utf-8') as f:
        print(f.read())
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question}
    ],
        max_tokens=8128,
        temperature=0,
        echo=False,
        stream=False,
        stop=None
    )
    answer = response['choices'][0]['message']['content']
    print("Zde je popis jak vylepšit váš instagram:")
    print(answer)

def main():
    profile_data()
    chat()
main()

   




