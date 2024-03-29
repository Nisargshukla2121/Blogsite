# Generated by Django 3.1.6 on 2021-02-16 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0040_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('available', 'Available to borrow'), ('borrowed', 'Borrowed by someone'), ('archived', 'Archived - not available anymore')], default='available', max_length=32)),
            ],
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
