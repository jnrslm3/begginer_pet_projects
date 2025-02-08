import requests
from bs4 import BeautifulSoup as BS



url = 'https://www.gonaturalenglish.com/1000-most-common-words-in-the-english-language/'
headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

response = requests.get(url, headers = headers)
soup = BS(response.text, 'html.parser')
words = soup.find_all('h4')

with open('words.txt', 'w') as word_file:
    for w in words:
        try:
            word = w.find('strong').text.strip()
        except AttributeError:
            continue
        
        if '–' in word:
            continue

        word_file.write(word + '\n')
        