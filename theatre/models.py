from django.db import models


class Play(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField('Actor', related_name='plays')
    genres = models.ManyToManyField('Genre', related_name='plays')


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    lsat_name = models.CharField(max_length=255)


class Genre(models.Model):
    name = models.CharField()
