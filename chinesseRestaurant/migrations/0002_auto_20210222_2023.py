# Generated by Django 3.1.7 on 2021-02-22 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinesseRestaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]