# Generated by Django 3.2.18 on 2023-03-22 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollsquestion',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
