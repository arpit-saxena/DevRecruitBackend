# Generated by Django 2.1.7 on 2019-03-10 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190310_0325'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='my_hash',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.TextField(blank=True),
        ),
    ]