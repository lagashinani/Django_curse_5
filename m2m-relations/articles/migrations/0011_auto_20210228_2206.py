# Generated by Django 3.1.2 on 2021-02-28 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20210228_2205'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['articlescope__is_main', 'topic'], 'verbose_name': 'Раздел', 'verbose_name_plural': 'Разделы'},
        ),
    ]
