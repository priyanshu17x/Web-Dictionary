import requests
from bs4 import BeautifulSoup as bs
import sys


while(1):
    print("\nEnter 0 to exit.")
    url = "http://www.dictionary.com/browse/"
    word = input("\nEnter the word : ")

    url= url+word


    if (word == "0"):
        exit(-1)


    r= requests.get(url)

    soup = bs(r.content, "lxml")


    try:
        pos= soup.findAll("span", {"class": "luna-pos"})[0].text
        definitions = soup.findAll("ol")
        meanings = definitions[0].findChildren("li", recursive=False)

    except:
        print("Word not found")

    

    print(word+ ":" + "\n" + pos)

    for (i, meaning) in enumerate (meanings):
        print(str(i+1), meaning.text)

        
