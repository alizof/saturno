# Generated by Django 5.1.2 on 2024-11-09 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_itenspedidovenda_produto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itenspedidovenda",
            name="status_produto",
            field=models.CharField(
                choices=[
                    (1, "Não Informado"),
                    (2, "Em Estoque"),
                    (3, "Sem Estoque"),
                    (4, "Em Producao"),
                    (5, "Fora de Linha"),
                ],
                default=1,
                max_length=1,
            ),
        ),
        migrations.AlterField(
            model_name="pedidovenda",
            name="status_pedido",
            field=models.CharField(
                choices=[
                    (1, "Pendente"),
                    (2, "Processando"),
                    (3, "Aguardando Pagamento"),
                    (4, "Pagamento Realizado"),
                    (5, "Em Separação"),
                    (6, "Aguardando a Coleta"),
                    (7, "Em Transporte"),
                    (8, "Entregue"),
                    (9, "Finalizado"),
                    (0, "Cancelado"),
                ],
                default=1,
                max_length=1,
            ),
        ),
    ]
