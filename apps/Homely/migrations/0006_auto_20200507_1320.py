# Generated by Django 3.0.6 on 2020-05-07 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homely', '0005_auto_20200507_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='reseñas',
            field=models.ManyToManyField(null=True, related_name='reseña', to='Homely.Reseña'),
        ),
    ]
