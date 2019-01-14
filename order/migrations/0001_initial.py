# Generated by Django 2.0 on 2019-01-11 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DropPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coffeename', models.CharField(blank=True, max_length=40)),
                ('coffee', models.CharField(blank=True, max_length=20)),
                ('place', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=40)),
                ('date', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
