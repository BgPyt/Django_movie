# Generated by Django 4.1.7 on 2023-02-28 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0007_director_remove_movie_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie_app.director'),
        ),
    ]