# Generated by Django 4.2.2 on 2023-06-25 02:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("calculation", "0002_transferamount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="balances",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="getdata",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="transferamount",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
