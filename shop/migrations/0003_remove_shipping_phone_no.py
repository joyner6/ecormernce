# Generated by Django 3.1.6 on 2021-02-17 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210216_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping',
            name='phone_no',
        ),
    ]
