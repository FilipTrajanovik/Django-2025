from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Translator(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    date_of_birth = models.DateField()


    def __str__(self):
        return f"{self.name} - {self.date_of_birth} - {self.nationality}"



class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.description}"



class Book(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    available_for_reading = models.BooleanField(default=True)
    date_published = models.DateField()
    added_by_user = models.ForeignKey(User, on_delete=models.CASCADE)
    num_pages = models.IntegerField()
    cover = models.ImageField(upload_to="./cover", null=True, blank=True)
    genres = models.ManyToManyField(Genre)
    translator = models.ManyToManyField(Translator)


    def __str__(self):
        return f"{self.title} - {self.date_published}"

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grade = models.IntegerField()
    comment = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.grade} - {self.comment}. By: {self.user}"
