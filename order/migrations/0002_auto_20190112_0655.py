# Generated by Django 2.0 on 2019-01-12 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='droppost',
            name='date',
            field=models.DateField(blank=True),
        ),
    ]
