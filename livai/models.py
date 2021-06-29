from django.db import models
from django.db.models.fields import BooleanField, CharField, DateField, EmailField, IntegerField, TextField
from pymongo.encryption import ClientEncryption

# Create your models here.

class Booking(models.Model):
    MOVIE_CHOICES = (
        ('Andhadhun','Andhadhun'),
        ('Dhamaal','Dhamaal'),
        ('Kal hona ho','Kal hona ho'),
        ('3 idiots','3 idiots'),
        ('Extraction','Extraction'),
        ('Bajrangi bhaijan','Bajrangi bhaijan'),
        ('Singham','Singham'),
        ('Delhi-6 ','Delhi-6 '),
        ('Dabbang','Dabbang'),
        ('The Shawshank Redemption','The Shawshank Redemption'),
        ('New york ','New york '),
        ('Special 26 ','Special 26 '),
        ('Hera pheri ','Hera pheri '),
        ('Citizen kane','Citizen kane'),
        ('10 things I hate about you','10 things I hate about you'),
        ('Dark knight ','Dark knight '),
        ('Suicide squad','Suicide squad'),
        ('Matru ki bijli ka mandola','Matru ki bijli ka mandola'),
        ('Demon Slayer-Mugen train','Demon Slayer-Mugen train'),
        ('Welcome','Welcome'),
    )

    name = models.CharField(max_length=100)
    persons = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    movie = models.CharField(choices=MOVIE_CHOICES, max_length=100)
    seats = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name

