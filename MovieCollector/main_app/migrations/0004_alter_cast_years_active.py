# Generated by Django 5.1.7 on 2025-04-04 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_cast_age_cast_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cast',
            name='years_active',
            field=models.CharField(max_length=100),
        ),
    ]
