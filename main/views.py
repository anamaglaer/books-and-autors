from django.shortcuts import render

from main.models import Autors, Book


# Create your views here.
def get_page(request):
    autor = Autors.objects.all()
    books = Book.objects.all()
    # print(books)
    for i in autor:
        print(i, i.book_set.all())
    #autor.book_set.all()

    # print(autor)
    # for i in autor:
    #     print('--------')
    #     print(i.name)
    #     print(i.famile)
    #     print(i.date)
    #     print(i.foto.url)


    context = {
        'autor': autor,
        'books': books
    }
    return render(request,'main.html', context)


def book_page(request, id):
    books = Book.objects.filter(autor_id=id)
    autor = Autors.objects.filter()
    print(books)
    context = {
        'autor': autor,
        'books': books,
        'id':id
    }
    return render(request, 'book.html', context)


def get_book_detail_page(request, book_id):
    book = Book.objects.get(id=book_id)
    print(book)

    context = {
        'book': book
    }
    return render(request, 'book_detail.html', context)
