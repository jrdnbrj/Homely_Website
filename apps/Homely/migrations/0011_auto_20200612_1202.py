# Generated by Django 3.0.6 on 2020-06-12 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homely', '0010_auto_20200612_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='descripcion',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='reseña',
            name='texto',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
