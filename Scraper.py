from googlesearch import search
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup


str = ("snopes fact check ")
ip= input("What would you like fact check on snopes? ")
str+=ip

urls = []

for url in search(str, stop=2):
     urls+=[url]

pages = []

for url in urls:
     if "https://www.snopes.com/fact-check" in url:
          pages+= [url]

for url in pages:
     print(url)

for url in pages:
     html = urlopen(url)
     soup = BeautifulSoup(html,features="html.parser")
     title = soup.title
     print(title)
     print(soup.find_all("div", class_="claim"))

     print(soup.find('h5'))




