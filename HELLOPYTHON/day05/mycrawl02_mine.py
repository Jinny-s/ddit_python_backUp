import requests
from bs4 import BeautifulSoup

file = open("ddeok.xml", "r", encoding="utf-8")

soup = BeautifulSoup(file, 'html.parser')

titles = soup.select("item > title, item > description")
for i, title in enumerate(titles):
    text = title.get_text().replace("<b>", "")
    print(text + "\n")

