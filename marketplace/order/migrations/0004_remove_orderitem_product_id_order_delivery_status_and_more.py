# Generated by Django 5.0 on 2023-12-07 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_id_orderitem'),
        ('product', '0001_initial'),
        ('user', '0002_alter_address_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='product_id',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('DELIVERED', 'Delivered'), ('CANCELLED', 'Failed')], default='PENDING', max_length=10),
        ),
        migrations.AddField(
            model_name='order',
            name='ship_to',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='shipping_address', to='user.address'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='product.product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='order.order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]