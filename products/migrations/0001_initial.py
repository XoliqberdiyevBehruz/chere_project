# Generated by Django 5.0.6 on 2024-06-18 06:43

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FreeProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('count', models.IntegerField()),
                ('free_count', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Free Product',
                'verbose_name_plural': 'Free Products',
            },
        ),
        migrations.CreateModel(
            name='GalleryPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('photo', models.FileField(upload_to='photos')),
            ],
            options={
                'verbose_name': 'Gallery Photo',
                'verbose_name_plural': 'Gallery Photos',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('free_count', models.IntegerField(default=0)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('status', models.TextField(choices=[('created', 'Created'), ('in_progres', 'In Progress'), ('on_the_way', 'On The Way'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], max_length=100)),
                ('status_changed_at', models.DateTimeField(auto_now=True)),
                ('product_price', models.BigIntegerField()),
                ('total_price', models.BigIntegerField()),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('name_ru', models.CharField(max_length=100, null=True)),
                ('name_uz', models.CharField(max_length=100, null=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('content_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('content_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('price', models.BigIntegerField()),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
