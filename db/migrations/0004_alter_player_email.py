# Generated by Django 4.0.2 on 2023-10-30 13:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0003_remove_race_choose_roles"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="email",
            field=models.EmailField(max_length=255),
        ),
    ]
