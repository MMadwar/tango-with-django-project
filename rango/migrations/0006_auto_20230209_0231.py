# Generated by Django 2.2.28 on 2023-02-09 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_category_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='Category',
            new_name='category',
        ),
    ]