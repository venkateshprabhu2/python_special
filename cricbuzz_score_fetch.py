#!/usr/bin/env python
#Note: The notification works on Macosx only. It's based on apple script.
#The program keeps running until terminated
import os

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))



import requests
from bs4 import BeautifulSoup
import pynotify
from time import sleep
url = "http://www.cricbuzz.com/livecricketscore/home-score-matches.xml"

while True: # Modify this condition to limit output
    r = requests.get(url)
    while r.status_code is not 200:
            r = requests.get(url)
    soup = BeautifulSoup(r.text)
    data = soup.find_all("header")
    notify("Live score", data[0].text) #Update the data[] parameter according to the match need to be notified.
    sleep(30) #Notify every 30 seconds
