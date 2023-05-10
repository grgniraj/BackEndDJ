# Generated by Django 4.2 on 2023-05-10 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('delivery_location', models.CharField(max_length=255)),
            ],
        ),
    ]
