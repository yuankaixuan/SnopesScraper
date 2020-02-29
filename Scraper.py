from googlesearch import search
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup


str = ("snopes fact check ")
ip= input("What would you like fact check on snopes? ")
str+=ip

urls = []

#change the stop value to the number of articles you want to scrape
for url in search(str, stop=2):
     urls+=[url]

pages = []

for url in urls:
     if "https://www.snopes.com/fact-check" in url:
          pages+= [url]

for url in pages:
     print(url)

titles = []
claims = []
ratings = []

for url in pages:
     html = urlopen(url)
     soup = BeautifulSoup(html,features="html.parser")
     title = soup.find("title").text
     titles+=[title]
     print(title)

     claim = soup.find("div", class_="claim").text
     c = claim.replace("\n",'')
     print(c)
     claims+= [c]

     rating = soup.find('h5').text
     print(rating)
     ratings+=[rating]

tcr = zip(titles,claims,ratings)

df = pd.DataFrame(tcr, columns=['Title','Claim','Rating'])

out = df.to_csv()

print(out)

df.to_csv("snopes.csv")










