# Generated by Django 3.2.15 on 2022-09-20 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapeamento_cultural', '0003_auto_20220915_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='artista',
            name='validade_rg',
            field=models.DateField(null=True, verbose_name='Validade RG'),
        ),
    ]
