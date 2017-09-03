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
    (1,'アニメ'),
    (2,'映画'),
    (3,'コズミックフロント'),
    (4,'勉強用'),
    (5,'クラッシック'),
    (6,'宇宙'),
    (7,'その他'),
    (8,'-------'),
    (9,'寺')
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

    def __str__(self):
        return self.name


class Disc(models.Model):
    name = models.CharField('CD,DVDの名前',max_length=255)
    genres = models.IntegerField('ジャンル',choices=JANRU_D,default=8)

    def __str__(self):
        return self.name


