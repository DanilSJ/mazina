# Generated by Django 5.0.6 on 2024-06-28 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_shirt_size_alter_shorts_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirt',
            name='discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='shorts',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]
