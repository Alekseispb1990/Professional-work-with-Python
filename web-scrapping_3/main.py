import re

import requests
from bs4 import BeautifulSoup
from user_agent import generate_navigator


BASE_URL = 'https://habr.com'


def get_soup(url):
    headers = generate_navigator()
    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, features='html.parser')
    return soup


def find_key_words(*key_words):
    articles_url = BASE_URL + '/ru/all/'
    articles = get_soup(articles_url).find_all(class_='tm-articles-list__item')
    for article in articles:
        article_href = article.find(class_='tm-article-snippet__title-link').attrs['href']
        article_url = BASE_URL + article_href
        article_text = get_soup(article_url).find(class_='tm-article-body').text
        pattern = rf"{'|'.join(key_words)}"
        result = re.search(pattern, article_text, flags=re.IGNORECASE)
        if result:
            article_title = article.find('h2').text
            print(f'Совпадение: {result.group()}')
            print(f"{article_title} - {article_url}")
            print()


if __name__ == '__main__':
    find_key_words('физика', 'python', 'scrapping', 'django', 'алгоритм', 'selenium',
                   'математика', 'собеседование', 'карьера', 'мотивация')
