# Generated by Django 4.0.2 on 2022-05-23 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('government', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importer',
            name='date_of_import',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
