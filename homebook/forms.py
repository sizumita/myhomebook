from django import forms
from django.forms import ModelForm
from .models import Book,Disc,booktag


class BookForm(ModelForm):
    """書籍のフォーム"""
    class Meta:
        model = Book
        fields = ('name', 'publisher', 'page','how','yonda','genre','place',)



class DiscForm(ModelForm):
    class Meta:
        model = Disc
        fields = ('name','genres')

class youtubeForm(forms.Form):
    douga = forms.URLField(max_length=255)

class booktagForm(ModelForm):
    """感想のフォーム"""
    class Meta:
        model = booktag
        fields = ('tag','how')