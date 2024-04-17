import requests
from bs4 import BeautifulSoup as b
import random

URL = 'https://www.anekdot.ru/last/good/'
def parser(url):
    r = requests.get(URL)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return[c.text for c in anekdots]

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)
