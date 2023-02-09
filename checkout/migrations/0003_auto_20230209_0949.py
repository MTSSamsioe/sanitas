# Generated by Django 3.2 on 2023-02-09 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0011_2_7'),
        ('products', '0006_alter_products_options'),
        ('checkout', '0002_auto_20230202_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_item',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djstripe.plan'),
        ),
        migrations.AlterField(
            model_name='order_item',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.products'),
        ),
    ]