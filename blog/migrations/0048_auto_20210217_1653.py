# Generated by Django 2.2.12 on 2021-02-17 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0047_auto_20210217_1550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='status',
            new_name='category',
        ),
    ]