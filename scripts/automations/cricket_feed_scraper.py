import requests

from bs4 import BeautifulSoup

feed_list = []

url = 'https://www.espncricinfo.com'

def get_data():
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    feeds = soup.find_all('a', class_='story-container')

    for feed in feeds:
        link = url + feed.get('href')
        title = feed.find('span', class_='story-title').get_text()
        content = feed.find('p', class_='story-description').get_text()
        img = feed.find('img', 'story-image').get('src')

        feed_list.append({
            'link': link,
            'title': title,
            'content': content,
            'img': img,
        })
    
    return feed_list
