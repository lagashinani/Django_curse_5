# Generated by Django 3.1.2 on 2021-02-28 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20210228_2157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlescope',
            options={},
        ),
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['topic'], 'verbose_name': 'Раздел', 'verbose_name_plural': 'Разделы'},
        ),
    ]
