# Generated by Django 3.1.5 on 2021-02-04 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_auto_20210204_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='uploader',
            field=models.ForeignKey(default=13, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
