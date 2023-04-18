# Generated by Django 4.1.6 on 2023-03-07 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tracker", "0009_record_owner"),
        ("tracker", "0009_record_overnight_parenting_record_stress_score"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(verbose_name="Tag Name")),
            ],
        ),
        migrations.AddConstraint(
            model_name="record",
            constraint=models.UniqueConstraint(
                fields=("owner", "date"), name="record_owner_date_unique"
            ),
        ),
        migrations.AddField(
            model_name="tag",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="record",
            name="tags",
            field=models.ManyToManyField(to="tracker.tag"),
        ),
        migrations.AddConstraint(
            model_name="tag",
            constraint=models.UniqueConstraint(
                fields=("owner", "name"), name="tag_owner_name_unique"
            ),
        ),
    ]
