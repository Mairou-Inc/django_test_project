# Generated by Django 3.2.8 on 2021-10-28 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='house',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер дома'),
        ),
    ]
