import random
import requests
from bs4 import BeautifulSoup


def getQuote():
    parsed_html = BeautifulSoup(requests.get('https://www.pensador.com/autor/naruto/').text, 'html.parser')
    result = parsed_html.find_all(class_="frase")
    return f'{random.choice(result).string} - UZUMAKI, Naruto.'