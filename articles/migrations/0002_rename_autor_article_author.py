# Generated by Django 4.1.4 on 2022-12-29 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='autor',
            new_name='author',
        ),
    ]
