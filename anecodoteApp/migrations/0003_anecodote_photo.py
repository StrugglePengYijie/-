# Generated by Django 2.2.4 on 2022-06-12 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anecodoteApp', '0002_auto_20220516_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='anecodote',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='anecodote/', verbose_name='展报'),
        ),
    ]
