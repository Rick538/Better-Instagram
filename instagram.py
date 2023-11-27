import instaloader
import time
import json
import re
from selenium.webdriver.common.by import By
import time
import json
from secret import USERNAME, PASSWORD
from selenium.webdriver.common.keys import Keys
import requests
from gpt4all import GPT4All
import pandas as pd
import openai

max_number = 8

def load_instagram(username):
    """Load data from instagram"""
    bot = instaloader.Instaloader()
    bot.load_session_from_file("karlito_podel9")
    profile_insta = instaloader.Profile.from_username(bot.context, username)
    return profile_insta

def clear_all_data():
    """Clear the json file named post_data"""
    with open('post_data.json', 'w', encoding='utf-8') as json_file:
        json_file.truncate()
    with open('formated_data.txt', 'w', encoding='utf-8') as f:
        f.close()

def profile_data():
    """Takes data from instagram profile and save them into json.file"""
    clear_all_data()
    post_data_list = []
    profile = load_instagram(username)
    about_user = {
        "Username:": profile.username,
        "Number of Posts:": profile.mediacount,
        "Following Count:": profile.followees,
        "Bio:": profile.biography,
        "External URL:": profile.external_url
    }
    post_data_list.append(about_user)
    post_number = 0
    for post in profile.get_posts():
        post_number += 1
        if post_number <= max_number:
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
            format_jason()

def format_jason():
    """This will formate data in json.file into readable text for chatgpt"""
    with open('post_data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        formated_json = re.sub(r'[:{}"\[\].,]','',json.dumps(data, indent=3))
        return formated_json

def format_data_to_text():
    df = pd.read_json (r'C:\Users\karel\OneDrive\Plocha\škola\zapocet z programka\post_data.json')
    df.to_csv (r'C:\Users\karel\OneDrive\Plocha\škola\zapocet z programka\formated_data.txt', index = False)
    with open('formated_data.txt', 'r', encoding='utf-8') as formated_text:
        form = re.sub(r'[:{}"\[\]\'.,]','',formated_text.read())
        word = form.split()
        words = 0
        words = len(word)
        formated_text.close()
    checking_tokens(words)

def checking_tokens(words):
    print(f"words: {words}")
    while words >= 240:
        global max_number
        max_number -= 1
        main()
    else:
        chat()

def chat():
    with open('formated_data.txt', 'r', encoding='utf-8') as data:
        data_for_chatgpt = data.read()
    question =  """
        Tell me what I should change on my Instagram profile to make it better, follow these points:
            1) username: do you think the username I'm using is creative and original, or should I change it?
            2) bio: is this bio original and if so why do you think so, if not then why and what should I change.
            3) hastags: are the hastags I have on my post good or should I change them, add new ones.
            4) headline: is the headline text good? or should I change it to something more informative, like information about the author or post, or where I am.
            5) date: should I post more in a short time or is this period good, should I post every day or week?
            Please answer the following questions in order so that they make sense and are legible.
        Write only answers and in points so it would be easier to understand.
        And finally, write down some understandable examples of how it could be a better.
        """ + str(data_for_chatgpt)

    openai.api_base = "http://localhost:4891/v1"
    openai.api_key = "not needed for a local LLM"
    model = "mistral-7b-openrca.Q4_0.gguf"

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

username = input("Enter your Instagram username: ")
def main():
    profile_data()
    format_data_to_text()
    chat()
main()