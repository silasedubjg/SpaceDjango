# Generated by Django 4.2.6 on 2023-10-18 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotografia_publicada_alter_fotografia_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]
