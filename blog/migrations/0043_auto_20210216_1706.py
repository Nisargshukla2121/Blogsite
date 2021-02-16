# Generated by Django 3.1.6 on 2021-02-16 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0042_auto_20210216_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('General', 'General blog'), ('Study', 'Study blog'), ('Technical', 'Technical Blog')], default='available', max_length=32)),
            ],
        ),
        migrations.DeleteModel(
            name='category',
        ),
    ]
