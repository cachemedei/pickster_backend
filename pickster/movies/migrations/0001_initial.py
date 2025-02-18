# Generated by Django 5.1 on 2025-02-18 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('year', models.IntegerField()),
                ('image', models.URLField()),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
