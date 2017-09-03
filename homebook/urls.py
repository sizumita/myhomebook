from django.conf.urls import url
from . import views as v

urlpatterns = [
    url(r'^booklist/$', v.book_list, name='book_list'),
    url(r'^booklisty/$',v.book_list_y,name='book_listy'),
    url(r'^booklistj/$',v.book_list_j,name='book_listj'),
    url(r'^book/add/$', v.book_edit, name='book_add'),
    url(r'^book/mod/(?P<book_id>\d+)/$', v.book_edit, name='book_mod'),
    url(r'^book/del/(?P<book_id>\d+)/$', v.book_del, name='book_del'),
    url(r'^$', v.TopPageView.as_view(), name='index'),
    url(r'^disc_list$', v.disc_list,name='disc_list'),
    url(r'^disc_edit$', v.disc_edit,name='disc_edit'),
    url(r'^disc/add/$', v.disc_edit, name='disc_add'),
    url(r'^disc/mod/(?P<disc_id>\d+)/$', v.disc_edit, name='disc_mod'),
    url(r'^disc/del/(?P<disc_id>\d+)/$', v.disc_del, name='disc_del'),
    url(r'^movied/$', v.youtube,name='videod'),
    url(r'^bookshelf$',v.book_shelf,name='bookshelf'),
    url(r'^bookinfo/(?P<book_id>\d+)/$',v.bookinfo, name='bookinfo'),

]