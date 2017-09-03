# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-03 03:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.IntegerField(choices=[(1, '生物'), (7, '小説'), (10, '-------'), (2, '宇宙'), (4, '地理'), (5, 'プログラミング'), (11, '染色'), (6, '辞典・辞書'), (8, '哲学'), (9, 'わからない'), (3, '歴史')], default=10, verbose_name='ジャンル'),
        ),
        migrations.AlterField(
            model_name='book',
            name='how',
            field=models.IntegerField(choices=[(4, 'なし'), (3, '済人'), (2, '父'), (1, '母')], default=4, verbose_name='誰の本か'),
        ),
        migrations.AlterField(
            model_name='book',
            name='yonda',
            field=models.IntegerField(choices=[(1, '既読'), (2, '未読'), (3, '途中')], default=2, verbose_name='本を読んだか'),
        ),
        migrations.AlterField(
            model_name='disc',
            name='genres',
            field=models.IntegerField(choices=[(3, 'コズミックフロント'), (6, '宇宙'), (7, 'その他'), (4, '勉強用'), (5, 'クラッシック'), (2, '映画'), (8, '-------'), (1, 'アニメ')], default=8, verbose_name='ジャンル'),
        ),
    ]