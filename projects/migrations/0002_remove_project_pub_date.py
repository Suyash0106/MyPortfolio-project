# Generated by Django 3.1.1 on 2020-10-18 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='pub_date',
        ),
    ]
