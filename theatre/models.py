from django.db import models


class Play(models.Model):
    id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()

