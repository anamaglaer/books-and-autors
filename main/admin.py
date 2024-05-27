from django.contrib import admin

from main.models import Autors, Book, Review

# Register your models here.
admin.site.register(Autors)
admin.site.register(Book)
admin.site.register(Review)
