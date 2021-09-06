import requests

from bs4 import BeautifulSoup
from csv import writer

response = requests.get(
    'https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find(class_='main-page-content')


links = posts.find('a')['href']
print(links)
