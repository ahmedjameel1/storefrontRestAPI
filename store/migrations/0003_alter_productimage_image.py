# Generated by Django 5.0.6 on 2024-05-21 13:37

import store.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='store/images', validators=[store.validators.validate_file_size]),
        ),
    ]
