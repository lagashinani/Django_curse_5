# Generated by Django 3.1.2 on 2021-02-28 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20210228_2155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlescope',
            options={'ordering': ['is_main']},
        ),
        migrations.AlterOrderWithRespectTo(
            name='articlescope',
            order_with_respect_to=None,
        ),
    ]
