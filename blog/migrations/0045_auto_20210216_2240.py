# Generated by Django 3.1.5 on 2021-02-16 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0044_auto_20210216_2225'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogCategory',
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(blank=True, choices=[('General', 'General blog'), ('Study', 'Study blog'), ('Technical', 'Technical Blog')], default='General', max_length=32),
        ),
    ]
