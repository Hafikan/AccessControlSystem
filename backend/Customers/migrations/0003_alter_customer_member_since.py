# Generated by Django 5.2 on 2025-04-04 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0002_alter_customer_options_alter_customer_member_since'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='member_since',
            field=models.DateField(blank=True, null=True),
        ),
    ]
