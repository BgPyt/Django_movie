# Generated by Django 4.1.7 on 2023-03-07 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0015_alter_feedback_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Жанр', max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='movie',
            name='artist',
            field=models.ManyToManyField(related_name='artist', to='movie_app.artist'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='director', to='movie_app.director'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(related_name='genre', to='movie_app.genre'),
        ),
    ]