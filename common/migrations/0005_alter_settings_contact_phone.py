# Generated by Django 4.2 on 2024-06-25 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_alter_settings_working_hours_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
