# Generated by Django 2.2.4 on 2022-04-29 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineApp', '0002_auto_20220427_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='line',
            name='description2',
            field=models.TextField(default=2, verbose_name='经典语录'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='line',
            name='description3',
            field=models.TextField(default=1, verbose_name='个人评价'),
            preserve_default=False,
        ),
    ]
