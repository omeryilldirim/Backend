# Generated by Django 4.2.1 on 2023-05-08 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fscohort', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='picture',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
