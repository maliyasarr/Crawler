import time

import requests
from bs4 import BeautifulSoup

from news import News


class NewsCrawler:

    def __init__(self, url, depth):
        self.url = url
        self.news_list = []
        self.comments = []

    def crawl(self):

        response = requests.get(self.url)
        soup_instance = BeautifulSoup(response.text, "html.parser")

        for news in soup_instance.find_all('div', attrs={'class': 'news'}):
            # soup_instance.find_all('span', class_='cat')
            for a in news.descendants:
                if a.name == 'div' and a.get('class', '') == ['desc']:
                    href = a.find("a").get("href")
                    tag = a.find('span', class_='cat').text

                    news_request = requests.get("http://www.hurriyet.com.tr" + href)
                    soup_instance = BeautifulSoup(news_request.content, "html.parser")

                    news = get_news_from_link(soup_instance, tag)

                self.news_list.append(news)

    # Ip adresimizin kaynak sitenin dikkatini cekememesi icin belli zaman dilimdeki request frekansi azaltıldı
    time.sleep(5)


def get_news_from_link(self, instance, tag):
    news_comments = []
    news_tags = []
    # Haberlerlerin taglerine gore siniflandirma yapıldı
    if tag == 'Gündem':
        title = instance.find('h1', class_='news-detail-title selectionShareable').text
        author = instance.find('div', class_='news-detail-author').text
        datetime = instance.find('div', class_='text-right').span.text
        modify_date = instance.find('span', class_='modify-date').time.text

    elif tag == 'Dünya' or tag == 'Ekonomi' or tag == 'Seyahat':
        title = instance.find('h1', class_='rhd-article-title').text
        text = instance.find('div', class_='rhd-all-article-detail').text
        datetime = instance.find('div', class_='rhd-time-box').span.text
        modify_date = instance.find('span', class_='rhd-time-box-text').time.text

        # TODO Comment contenti icerisindeki taglere erisim saglayamadım
        # for comment in instance.find_all("div", {"class": "comment-box news-item list-edit-text"}):
        #     comment_author = comment.find('span', class_='comment-box-member-info-title').text
        #     comment_datetime = comment.find('span', class_='comment-box-member-info-date').text
        #     comment_text = comment.find('textarea', class_='comment-box-area 004').text
        #
        #     comment = Comment(comment_text, comment_author, comment_datetime, 0, 0)
        #     news_comments.append(comment)

        for ultag in instance.find_all("ul", {"class": "rhd-article-tag-box cf"}):
            for litag in ultag.find_all('li', class_='rhd-article-tag-item'):
                news_tags.append(litag.text)


    elif tag == 'Spor Videoları' or tag == 'Video':
        title = instance.find('h1', class_='video-title').text
        text = instance.find('div', class_='video-description').text
        datetime = instance.find('div', class_='date').time.text
        modify_date = ""

        for ultag in instance.find_all("ul", {"class": "video-layers"}):
            for litag in ultag.find_all('li'):
                news_tags.append(litag.text)

    elif tag == 'Kelebek':
        return

    else:
        title = instance.find('h2', class_='news-detail-title selectionShareable local-news-title').text
        author = instance.find('div', class_='news-detail-author').span.text
        datetime = instance.find('div', class_='text-right').span.text
        modify_date = instance.find('div', class_='modify-date').time.text

    news = News(datetime, modify_date, author, title, text, news_tags, news_comments)

    return news


crawler = NewsCrawler('http://www.hurriyet.com.tr/index/?d=20180519', 0)
crawler.crawl()

for news in crawler.news_list:
    print(news)
