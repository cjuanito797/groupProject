# Generated by Django 3.1.7 on 2021-02-24 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinesseRestaurant', '0010_auto_20210224_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(default='Item Category', max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.CharField(blank=True, default='759547', editable=False, max_length=6, primary_key=True, serialize=False, unique=True),
        ),
    ]