from light_progress.commandline import ProgressBar
from time import sleep
import re
import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E5%A5%B3%E6%80%A7%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%97%E3%81%AE%E4%B8%80%E8%A6%A7#2010%E5%B9%B4%E4%BB%A3'

    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')

    links = []
    for li in soup.find_all('li'):
        if li.a:
            if li.a.get('href').startswith('/wiki/'):
                links.append(f'https://ja.wikipedia.org{li.a.get("href")}')

    for link in ProgressBar.generation(links):
        html = requests.get(link).text
        sleep(1)
        if '年2月22日' in str(html):
            print(link)


if __name__ == '__main__':
    main()
