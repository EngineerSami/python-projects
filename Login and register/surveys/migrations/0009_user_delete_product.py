# Generated by Django 5.1.2 on 2024-11-14 09:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0008_product_delete_show'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator(message='Only letters allowed', regex='^[a-zA-Z]*$')])),
                ('last_name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator(message='Only letters allowed', regex='^[a-zA-Z]*$')])),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
