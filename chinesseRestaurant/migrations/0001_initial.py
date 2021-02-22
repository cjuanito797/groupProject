# Generated by Django 3.1.7 on 2021-02-22 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('firstName', models.CharField(max_length=35)),
                ('lastName', models.CharField(max_length=35)),
                ('address', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True)),
                ('customer_phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('name', models.CharField(max_length=25)),
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True)),
                ('orderQty', models.CharField(max_length=100)),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('deliveryPref', models.CharField(choices=[('delivery', 'Delivery'), ('pickup', 'Pickup')], default='pickup', max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='chinesseRestaurant.customer')),
            ],
        ),
    ]