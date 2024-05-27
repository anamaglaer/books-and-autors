from django.db import models

# Create your models here.

class Autors(models.Model):
    name = models.CharField(max_length=255)
    famile = models.CharField(max_length=255)
    date = models.DateField()
    foto = models.ImageField()

    def __str__(self):
        #  return self.famile
        return f'{self.name} {self.famile}'

class Book(models.Model):
    name = models.CharField(max_length=255)
    date_of_publish = models.DateField()
    short_description = models.TextField()
    image = models.ImageField()

    autor = models.ForeignKey("Autors", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Review(models.Model):
    review = models.TextField()

    book = models.ForeignKey("Book", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.book}'