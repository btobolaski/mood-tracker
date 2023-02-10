# Generated by Django 4.1.6 on 2023-02-10 02:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0006_record_sex_drive"),
    ]

    operations = [
        migrations.AddField(
            model_name="record",
            name="irritability",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "None"),
                    (1, "A little"),
                    (2, "A moderate amount"),
                    (3, "A large amount"),
                    (4, "An excessive amount"),
                ],
                default=0,
                validators=[
                    django.core.validators.MaxValueValidator(4),
                    django.core.validators.MinValueValidator(0),
                ],
            ),
        ),
    ]