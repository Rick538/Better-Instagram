# Instagram Improvement Assistant
## Introduction

It uses the Instaloader library to gather data from a specified Instagram profile and then uses OpenAI's ChatGPT to provide recommendations for enhancing the profile.
The gathered data includes general information about the user, such as the username, number of posts, following count, bio, and external URL.
Additionally, it retrieves information about the user's recent posts, including post ID, date, caption, likes count, comments count, location, hashtags.
Then it will give you some examples of how can be your instagram profile improved.

## Overview

Using instaloader to load your instagram profile and save this informations into json file.

Converted data from json file into text file and formate them by deleting all the unnecessary characters.

Checks the amount of words that is in the text file because of the max tokens in the prompt, if there is a more then a fixed number of words the program will restart and remove 1 post from the json file, until there is enough space for the data.

Sends the data include the question, thanks to which Ai will tell you how to improve your Instagram.

Gets the answer and print it on the screen.

## Dependencies

* Instaloader: For accessing Instagram profile data.

* Pandas: For data manipulation.

* Openai: OpenAI's GPT-3.5 API for natural language processing.

## Installation

Firefox driver: [Download](https://github.com/mozilla/geckodriver/releases)

You need to install this geckodriver for Firefox.

Gpt4all: [Download](https://gpt4all.io/index.html)

Before you run the program you need to run this and install the Mistral OpenOrca model.











