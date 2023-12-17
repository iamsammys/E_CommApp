# Generated by Django 5.0 on 2023-12-17 20:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
        ('product', '0001_initial'),
        ('user', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('delivery_status', models.CharField(choices=[('PENDING', 'Pending'), ('DELIVERED', 'Delivered'), ('CANCELLED', 'Failed')], default='PENDING', max_length=10)),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='order', to='cart.cart')),
                ('ship_to', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='shipping_address', to='user.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField(default=0.0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='product.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
