# Generated by Django 2.2.12 on 2021-02-17 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0046_auto_20210217_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('General', 'General blog'), ('Study', 'Study blog'), ('Technical', 'Technical Blog')], max_length=32),
        ),
    ]
