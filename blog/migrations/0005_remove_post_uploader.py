# Generated by Django 3.1.5 on 2021-02-04 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_uploader'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='uploader',
        ),
    ]
