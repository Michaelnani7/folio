# Generated by Django 2.1.5 on 2020-02-11 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='body',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
