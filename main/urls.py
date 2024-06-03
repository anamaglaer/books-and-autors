
from django.urls import path

from main.views import get_page, book_page, get_book_detail_page, index_page

urlpatterns = [
    path('main/', get_page, name='main'),
    path('book/<int:id>/', book_page, name='book'),
    path('book_detail/<int:book_id>/', get_book_detail_page, name='book_detail'),
    path('index/', index_page, name='index')
]