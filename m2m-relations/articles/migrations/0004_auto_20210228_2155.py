# Generated by Django 3.1.2 on 2021-02-28 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20210228_2016'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='articlescope',
            order_with_respect_to='is_main',
        ),
    ]
