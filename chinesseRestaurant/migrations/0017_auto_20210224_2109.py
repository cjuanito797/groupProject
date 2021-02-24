# Generated by Django 3.1.7 on 2021-02-24 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinesseRestaurant', '0016_auto_20210224_2102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='someValue', max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='item',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='someValue', max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.CharField(blank=True, default='486906', editable=False, max_length=6, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterIndexTogether(
            name='item',
            index_together={('id', 'slug')},
        ),
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
    ]
