# Generated by Django 5.0.8 on 2024-08-07 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_no_of_guests_alter_menu_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='inventory',
            field=models.SmallIntegerField(),
        ),
    ]
