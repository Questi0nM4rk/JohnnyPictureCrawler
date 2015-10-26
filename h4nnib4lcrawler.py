__author__ = 'Lorio'

from bs4 import BeautifulSoup
import requests
import requests.exceptions
import re


maxPages = 92500
counter = 91727

global maxPages
global counter

while counter != maxPages:
    counter += 1
    print("Done" + " Event " + str(counter))
    treasure = ["lilrcfall", "lilrcfall15", "lilrcfall2015", "lilrc",]

    url = "http://codyharris.morephotos.com/mp_client/login.asp?eventid=" + str(counter) +"&eventstatus=0&categories=" \
            "yes&keywords2=no&groupid=0&bw=true&sep=true&ckw=false"

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    gData = soup.find_all("td", {"class": "small4v"})

    for i in gData:
        tagged = i.find_all("strong")
        for item in tagged:
            cleanText = item.text
    shitWords = re.sub("[^\w]", " ",  cleanText).split()
    compareList = []
    print(shitWords)
    for word in shitWords:
        compareList.append(word.lower())
        for a in compareList:
            for b in treasure:
                if a == b:

                    counter = maxPages

f = open("Imagesfound.txt", "w")
f.write(str(url))
print("FOUND IT!!! " + str(url))





