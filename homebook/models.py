from django.db import models
from django.db.models import Q
import re
# Create your models here.
from django.utils.timezone import now









HOW = {
    (1,'母'),
    (2,'父'),
    (3,'済人'),
    (4,'なし')
}

YONDA = {
    (1,'既読'),
    (2,'未読'),
    (3,'途中')
}

JANRU = {
    (1,'生物'),
    (2,'宇宙'),
    (3,'歴史'),
    (4,'地理'),
    (5,'プログラミング'),
    (6,'辞典・辞書'),
    (7,'小説'),
    (8,'哲学'),
    (9,'わからない'),
    (10,'-------'),
    (11,'染色')
}

JANRU_D = {
    (1,'CD'),
    (2,'DVD'),
    (3,'BD')
}

PLS = {
    (1,'１階'),
    (2,'２階'),
    (3,'不定')
}


class Book(models.Model):
    """書籍"""
    name = models.CharField('本の名前',max_length=255)
    publisher = models.CharField('出版社',max_length=255,blank=True)
    page = models.IntegerField('ページ数',blank=True,default=0)
    how = models.IntegerField('誰の本か',choices=HOW,default=4)
    yonda = models.IntegerField('本を読んだか',choices=YONDA,default=2)
    genre = models.IntegerField('ジャンル',choices=JANRU,default=10)
    date = models.DateField('登録した日付',default=now)
    place = models.IntegerField('場所',choices=PLS,default=3)

    def __str__(self):
        return self.name


class Disc(models.Model):
    name = models.CharField('CD,DVDの名前',max_length=255)
    genres = models.IntegerField('種類',choices=JANRU_D,blank=True)

    def __str__(self):
        return self.name

class booktag(models.Model):
    book = models.ForeignKey(Book, verbose_name='本', related_name='tags')
    tag = models.CharField('タグのページ',max_length=100)
    how = models.IntegerField('誰のタグか',choices=HOW,default=4)
    def __str__(self):
        return self.tag
