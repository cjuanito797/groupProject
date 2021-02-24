# Generated by Django 3.1.7 on 2021-02-24 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinesseRestaurant', '0011_auto_20210224_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='photo',
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.CharField(blank=True, default='140462', editable=False, max_length=6, primary_key=True, serialize=False, unique=True),
        ),
    ]
