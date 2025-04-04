# Generated by Django 5.1.7 on 2025-04-03 22:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_cast'),
    ]

    operations = [
        migrations.AddField(
            model_name='cast',
            name='age',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='cast',
            name='movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.movie'),
        ),
    ]
