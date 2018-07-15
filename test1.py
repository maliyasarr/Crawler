import requests
from bs4 import BeautifulSoup
from news import Comment

news_request = requests.get(
    'http://www.hurriyet.com.tr/video/15-temmuz-destaninin-2-yili-40897100')
soup_instance = BeautifulSoup(news_request.content, "html.parser")

news_comments = []
news_tags = []

title = soup_instance.find('h1', class_='video-title').text
text = soup_instance.find('div', class_='video-description').text
datetime = soup_instance.find('div', class_='date').time.text
modify_date = ""

for ultag in soup_instance.find_all("ul", {"class": "video-layers"}):
    for litag in ultag.find_all('li'):
        news_tags.append(litag.text)

print("")
