# Generated by Django 5.1.2 on 2024-11-14 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0009_user_delete_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
