# Generated by Django 3.1.6 on 2021-02-10 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20210210_0554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='auth',
        ),
    ]
