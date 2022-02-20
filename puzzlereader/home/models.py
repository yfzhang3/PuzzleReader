from tkinter.tix import Select
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
GENRES = (
    ('Action', 'Action'), ('Fiction', 'Fiction'), ('Classics', 'Classics'), ('Mystery',
                                                                             'Mystery'), ('Comic', 'Comic'), ('Nonfiction', 'Nonfiction'), ('Fantasy', 'Fantasy')
)


class Book(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=25, default="user")
    title = models.CharField(max_length=30)
    genre = models.CharField(max_length=200,
                             choices=GENRES,
                             default='None')
    summary = models.CharField(max_length=500)
    # this doesn't work
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    book_cover = models.ImageField(
        upload_to="media/", null=True, blank=True)
    #image = models.ImageField(upload_to="images/",default="images/221182406_998264654304104_3219754300096054984_n.png")

    def __str__(self):
        return self.name
