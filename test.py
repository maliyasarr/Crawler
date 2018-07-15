import requests
from bs4 import BeautifulSoup
from news import Comment

news_request = requests.get(
    'http://www.hurriyet.com.tr/seyahat/inci-koleliginden-petrolun-efendiligine-40895467')
soup_instance = BeautifulSoup(news_request.content, "html.parser")

news_comments = []
news_tags = []

title = soup_instance.find('h1', class_='rhd-article-title').text
text = soup_instance.find('div', class_='rhd-all-article-detail').text
datetime = soup_instance.find('div', class_='rhd-time-box').span.text
modify_date = soup_instance.find('div', class_='rhd-time-box').next.next_sibling.time.text

# for comment in soup_instance.find_all("div", {"class": "commenty-view"}):
#     for a in comment.descendants:
#         comment_author = a.find('span', class_='comment-box-member-info-title').text
#         comment_datetime = a.find('span', class_='comment-box-member-info-date').text
#         comment_text = a.find('textarea', class_='comment-box-area 004').text
#
#     comment = Comment(comment_text, comment_author, comment_datetime, 0, 0)
#     news_comments.append(comment)

# for tag in soup_instance.find_all("ul", {"class": "rhd-article-tag-box cf"}):
#     for a in tag.descendants:
#         tag = a.find('li', class_='rhd-article-tag-item').a.text
#         news_tags.append(tag)

for ultag in soup_instance.find_all("ul", {"class": "rhd-article-tag-box cf"}):
    for litag in ultag.find_all('li', class_='rhd-article-tag-item'):
        news_tags.append(litag.text)

print("")
