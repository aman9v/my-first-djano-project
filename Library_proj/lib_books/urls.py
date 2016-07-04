from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.BookList.as_view()),
    url(r'^new_book$', views.new_book, name='new_book'),
    url(r'(?P<pk>\d+)/$', views.BookDetail.as_view(),name='detail'),
    url(r'^register/$', views.NewUserView.as_view(), name="register"),
]
# name is an identification for the corresponding view
# url(r'(?P<library_pk>\d+)/(?P<book_pk>\d+)/$', views.book_detail,
#     name='detail'),
