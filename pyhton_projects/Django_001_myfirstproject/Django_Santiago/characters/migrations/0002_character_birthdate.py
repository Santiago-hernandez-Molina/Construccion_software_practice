# Generated by Django 3.2.8 on 2021-11-01 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='birthdate',
            field=models.DateTimeField(default='2019-01-01'),
            preserve_default=False,
        ),
    ]