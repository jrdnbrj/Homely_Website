# Generated by Django 3.0.6 on 2020-05-07 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homely', '0006_auto_20200507_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]