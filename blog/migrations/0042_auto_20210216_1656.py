# Generated by Django 3.1.6 on 2021-02-16 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0041_auto_20210216_1607'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='category',
        ),
    ]