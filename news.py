class News:

    def __init__(self, datetime, modify_date, author, title, text, tags, comments):
        self.datetime = datetime
        self.modify_date = modify_date
        self.author = author
        self.title = title
        self.text = text
        self.tags = tags
        self.comments = comments

    # def add_commment(self, comment):
    #     assert isinstance(comment, Comment)
    #     assert comment.name not in self.comments
    #     self.comments[comment.name] = comment

    def __str__(self):
        return (" Datetime: " + self.datetime +
                "\r\n Author: " + self.author +
                "\r\n Title: " + self.title +
                "\r\n Text: " + self.text +
                "\r\n Comments:")

    # TODO : Method gözden gecilirilecek
    def reformatList(self, list):
        for object in list:
            print(object)


class Comment:

    def __init__(self, text, author, datetime, likeCount, unlikeCount):
        self.text = text
        self.author = author
        self.datetime = datetime
        self.likeCount = likeCount
        self.unlikeCount = unlikeCount
        self.link_with_news(news)

    def link_with_news(self, news):
        assert isinstance(news, News)
        self.news = news
        news.add_commment(self)

    def __str__(self):
        return ("Text: " + self.text.encode('UTF-8') +
                "\r\n Title: " + self.title.encode('UTF-8') +
                "\r\n Author: " + self.author.encode('UTF-8') +
                "\r\n Datetime: " + self.datetime.encode('UTF-8') +
                "\r\n Number of Like : " + self.likeCount.encode('UTF-8') +
                "\r\n Number of Unlike " + self.unlikeCount.encode('UTF-8'))
