# Generated by Django 4.1.5 on 2023-02-01 04:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[
                 ('D', 'Delivered'), ('ND', 'Not Delivered')], max_length=2)),
                ('amount', models.PositiveIntegerField()),
                ('payment', models.CharField(choices=[
                 ('Card', 'Card'), ('Cash', 'Cash')], max_length=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('delivered_at', models.DateTimeField()),
                ('author',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='orders',
                                   to=settings.AUTH_USER_MODEL)),
                ('product',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='orders',
                                   to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('is_favorite', models.BooleanField(default=False)),
                ('author',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='favorites',
                                   to=settings.AUTH_USER_MODEL)),
                ('product',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='favorites',
                                   to='product.product')),
            ],
        ),
    ]
