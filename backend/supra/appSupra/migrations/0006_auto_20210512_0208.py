# Generated by Django 3.1.7 on 2021-05-12 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSupra', '0005_auto_20210512_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integrantes',
            name='numeroDocumento',
            field=models.CharField(max_length=50),
        ),
    ]
