# Generated by Django 2.2.4 on 2022-06-14 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anecodoteApp', '0003_anecodote_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anecodote',
            options={'ordering': ['-publishDate'], 'verbose_name': '逸闻中心', 'verbose_name_plural': '逸闻中心'},
        ),
    ]
