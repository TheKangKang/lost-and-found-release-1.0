# Generated by Django 5.0.2 on 2024-03-18 14:02

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Found",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        db_column="id", primary_key=True, serialize=False
                    ),
                ),
                (
                    "found_name",
                    models.CharField(db_column="found_name", max_length=100),
                ),
                ("place", models.CharField(db_column="address", max_length=200)),
                ("found_date", models.DateField(db_column="found_date")),
                ("username", models.CharField(db_column="username", max_length=100)),
                ("mobile", models.CharField(db_column="mobile", max_length=100)),
                ("is_return", models.CharField(db_column="is_return", max_length=100)),
                (
                    "image",
                    models.CharField(db_column="image", max_length=200, null=True),
                ),
            ],
            options={
                "db_table": "Found",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Lost",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        db_column="id", primary_key=True, serialize=False
                    ),
                ),
                ("lost_name", models.CharField(db_column="lost_name", max_length=100)),
                ("place", models.CharField(db_column="address", max_length=200)),
                ("lost_date", models.DateField(db_column="lost_date")),
                ("username", models.CharField(db_column="username", max_length=100)),
                ("mobile", models.CharField(db_column="mobile", max_length=100)),
                ("is_return", models.CharField(db_column="is_return", max_length=100)),
                (
                    "image",
                    models.CharField(db_column="image", max_length=200, null=True),
                ),
            ],
            options={
                "db_table": "Lost",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Manager",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        db_column="id", primary_key=True, serialize=False
                    ),
                ),
                ("username", models.CharField(db_column="username", max_length=100)),
                ("password", models.CharField(db_column="password", max_length=100)),
                ("real_name", models.CharField(db_column="real_name", max_length=100)),
                (
                    "gender",
                    models.CharField(
                        choices=[("男", "男"), ("女", "女")],
                        db_column="gender",
                        max_length=100,
                    ),
                ),
                ("mobile", models.CharField(db_column="mobile", max_length=100)),
                ("email", models.CharField(db_column="email", max_length=100)),
                ("address", models.CharField(db_column="address", max_length=200)),
                (
                    "image",
                    models.CharField(db_column="image", max_length=200, null=True),
                ),
            ],
            options={
                "db_table": "manager",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        db_column="id", primary_key=True, serialize=False
                    ),
                ),
                ("username", models.CharField(db_column="username", max_length=100)),
                ("password", models.CharField(db_column="password", max_length=100)),
                ("real_name", models.CharField(db_column="real_name", max_length=100)),
                (
                    "gender",
                    models.CharField(
                        choices=[("男", "男"), ("女", "女")],
                        db_column="gender",
                        max_length=100,
                    ),
                ),
                ("mobile", models.CharField(db_column="mobile", max_length=100)),
                ("email", models.CharField(db_column="email", max_length=100)),
                ("address", models.CharField(db_column="address", max_length=200)),
                (
                    "image",
                    models.CharField(db_column="image", max_length=200, null=True),
                ),
            ],
            options={
                "db_table": "user",
                "managed": True,
            },
        ),
    ]
