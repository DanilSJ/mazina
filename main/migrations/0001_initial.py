# Generated by Django 5.0.6 on 2024-06-28 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('company', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('size', models.CharField(default='L', max_length=10)),
                ('price', models.IntegerField(default=0)),
                ('img', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Shorts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('company', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('size', models.CharField(default='L', max_length=10)),
                ('price', models.IntegerField(default=0)),
                ('img', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Sneakers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('company', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('size', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('discount', models.IntegerField(default=0)),
                ('img', models.ImageField(upload_to='img')),
            ],
        ),
    ]