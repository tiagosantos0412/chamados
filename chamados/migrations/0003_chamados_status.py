# Generated by Django 5.0.1 on 2024-01-16 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamados', '0002_remove_chamados_anexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamados',
            name='status',
            field=models.IntegerField(choices=[(1, 'Novo'), (2, 'Em Resolução'), (3, 'Resolvido')], default=1),
            preserve_default=False,
        ),
    ]
