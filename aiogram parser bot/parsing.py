import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv


def pars_gazeta(category):
    list_news = []
    load_dotenv()
    URL = os.getenv('URL')
    HOST = os.getenv('HOST')
    HEADERS = {
        'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    html = requests.get(URL + category, headers=HEADERS).text
    soup = BeautifulSoup(html, 'html.parser')

    main_art = soup.find_all('div', class_='nblock')
    for art in main_art[:3]:
        images = art.find('img', class_='lazy').get('data-src')
        data_time = ' '.join(art.find('div', class_='ndt').get_text().split())
        title = ' '.join(art.find('h3').get_text().split())
        info = ' '.join(art.find('p').get_text().split())
        link = HOST + art.find('a').get('href')

        list_news.append({
            'images': images,
            'data_time': data_time,
            'title': title,
            'info': info,
            'link': link
        })
    return list_news
