# Generated by Django 4.1.6 on 2023-04-17 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_cart_profile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
    ]