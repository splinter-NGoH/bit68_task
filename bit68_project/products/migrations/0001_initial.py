# Generated by Django 3.2.11 on 2022-09-17 03:08

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_name', models.CharField(max_length=200, unique=True, verbose_name='product name')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='product_name', unique=True)),
                ('description', models.TextField(blank=True, max_length=500, verbose_name='description')),
                ('price', models.IntegerField(verbose_name='price')),
                ('image', models.ImageField(default='/default_product.png', upload_to='', verbose_name='image')),
                ('stock', models.IntegerField(verbose_name='stock')),
                ('is_available', models.BooleanField(default=True, verbose_name='is available')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
    ]
