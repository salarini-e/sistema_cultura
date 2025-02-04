# Generated by Django 3.2.15 on 2022-09-15 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapeamento_cultural', '0002_auto_20220915_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='artista',
            name='portfolio',
            field=models.FileField(blank=True, null=True, upload_to='portfolio', verbose_name='Portfólio'),
        ),
        migrations.AddField(
            model_name='artista',
            name='rg',
            field=models.FileField(blank=True, null=True, upload_to='rg', verbose_name='RG'),
        ),
        migrations.AlterField(
            model_name='artista',
            name='banco',
            field=models.CharField(blank=True, choices=[('001', 'Banco do Brasil - 001'), ('033', 'Banco Santander - 033'), ('104', 'Caixa Econômica Federal - 104'), ('237', 'Banco Bradesco - 237'), ('341', 'Banco Itaú - 341'), ('399', 'HSBC - 399'), ('745', 'Banco Citibank - 745'), ('260', 'Nu Bank - 260'), ('out', 'Outro')], default='', max_length=3, null=True, verbose_name='Banco (Conta Corrente):'),
        ),
        migrations.AlterField(
            model_name='informacoesextras',
            name='forma_atuacao',
            field=models.ManyToManyField(blank=True, to='mapeamento_cultural.Forma_insercao_Atuacao', verbose_name='Forma de inserção da atividade artístico-cultural'),
        ),
    ]
