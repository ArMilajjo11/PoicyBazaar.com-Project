# Generated by Django 3.0.5 on 2021-06-04 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='chomu',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
