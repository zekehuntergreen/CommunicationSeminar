# Generated by Django 2.0 on 2018-07-28 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ComSemApp', '0004_auto_20180728_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worksheet',
            name='released',
        ),
        migrations.AddField(
            model_name='worksheet',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ComSemApp.Teacher'),
        ),
    ]
