from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    favorite_genre = models.CharField(max_length = 64, null = True ,blank = True)
    favorite_band = models.CharField(max_length = 64, null = True ,blank = True)
    favorite_song = models.CharField(max_length = 64, null = True ,blank = True)

    def __str__(self):
        return self.email