from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth import get_user_model
from django.urls import reverse


class Album(models.Model):
    title = CharField(max_length = 64)
    band = CharField(max_length = 64)
    release_year = IntegerField()
    description = TextField()
    rating = IntegerField()
    author = ForeignKey(get_user_model(), on_delete=CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('album_detail', args = [str(self.pk)])