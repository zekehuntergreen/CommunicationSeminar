# Generated by Django 2.0.12 on 2020-04-14 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComSemApp', '0014_reviewattempt'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentattempt',
            name='audioCorrect',
            field=models.NullBooleanField(default=None),
        ),
    ]
