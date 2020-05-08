# Generated by Django 2.2.12 on 2020-05-08 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name="Author's name")),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name="Book's name")),
                ('edition', models.CharField(max_length=15, verbose_name='Edition')),
                ('publication_year', models.DateField(verbose_name='Year of the publication')),
                ('authors', models.ManyToManyField(to='catalog.Author')),
            ],
        ),
    ]