# Generated by Django 3.1.4 on 2021-11-17 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_favorite_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='favorite_band',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='favorite_song',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
