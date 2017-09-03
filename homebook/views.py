import urllib.request
import urllib.parse
from .models import Book,Disc
from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.views import generic
from .forms import BookForm,DiscForm,youtubeForm
import json
import urllib.request
import urllib.parse
import re
import urllib
import youtube_dl
from django.db.models import Q
import re

options = {
  'format': 'bestaudio[ext=mp3]/bestaudio[ext=m4a]/bestaudio'
}

#  Create your views here.


class GetURL:
    def geturl(self):
        amazon = 'https://www.amazon.co.jp/s/url=search-alias%3Daps&field-keywords='
        params = urllib.parse.urlencode({'q': self})
        url = 'https://www.googleapis.com/books/v1/volumes?' + params
        a = urllib.request.urlopen(url)
        data = json.loads(a.read().decode('utf-8'))
        url = []
        get = []
        try:
            for item in data['items']:
                iIs = item['volumeInfo']['industryIdentifiers']
                for iI in iIs:
                    url.append(iI['identifier'])
            r = re.compile('^[0-9]+$')
            for x in filter(r.match, url):
                get.append(amazon + x)
            return get[0]
        except:
            return 'https://www.amazon.co.jp'

class geta:
    def getara(self):
        try:
            ara = ''
            params = urllib.parse.urlencode({'q': self})
            url = 'https://www.googleapis.com/books/v1/volumes?' + params
            a = urllib.request.urlopen(url)
            data = json.loads(a.read().decode('utf-8'))
            b = []
            items = data['items']
            datas = items[0]['volumeInfo']['description']
            return datas
        except:
            return 'なし'


def book_list(request):
    """本の一覧"""
    books = Book.objects.all().order_by('name')
    return render(request,
                  'homebook/book_list.html',
                  {'books' : books})


def book_list_y(request):
    books = Book.objects.all().order_by('-yonda')
    return render(request,
                  'homebook/book_lists.html',
                  {'books' : books})

def book_list_j(request):
    books = Book.objects.all().order_by('genre')
    return render(request,
                  'homebook/book_lists.html',
                  {'books' : books})

def book_list_p(request):
    books = Book.objects.all().order_by('place')
    return render(request,
                  'homebook/book_lists.html',
                  {'books' : books})


def book_shelf(request):
    book = Book.objects.all().order_by('name')
    return render(request,
                  'homebook/book_shelf.html',
                  {'book' : book })


class TopPageView(generic.TemplateView):
    template_name = "homebook/index.html"


def book_edit(request, book_id=None):
    """書籍の編集"""

    if book_id:
        book = get_object_or_404(Book, pk=book_id)
    else:
        book = Book()

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('homebook:book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'homebook/book_edit.html', dict(form=form, book_id=book_id))

def bookinfo(request, book_id=None):
    if book_id:
        book = get_object_or_404(Book, pk=book_id)
    else:
        book = Book.objects.get(book_id)
    return render(request, 'homebook/book_info.html',
                  { 'book' : book },)

def book_del(request, book_id):
    """書籍の削除"""
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('homebook:book_list')



def disc_list(request):
    disc = Disc.objects.all().order_by('name')
    return render(request,'homebook/disc_list.html',{'disc' : disc})


def disc_edit(request, disc_id=None):
    """書籍の編集"""

    if disc_id:
        disc = get_object_or_404(Disc, pk=disc_id)
    else:
        disc = Disc()

    if request.method == 'POST':
        form = DiscForm(request.POST, instance=disc)
        if form.is_valid():
            disc = form.save(commit=False)
            disc.save()
            return redirect('homebook:disc_list')
    else:
        form = DiscForm(instance=disc)

    return render(request, 'homebook/disc_edit.html', dict(form=form, disc_id=disc_id))


def disc_del(request, disc_id):
    """書籍の削除"""
    disc = get_object_or_404(Disc, pk=disc_id)
    disc.delete()
    return redirect('homebook:disc_list')

def youtube(request):
    form = youtubeForm
    if request.method == 'POST':
            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([str(request.POST)])
                return redirect('homebook:book_list')

    return render(request,
                  'homebook/youtube.html',
                  {'form':form})

