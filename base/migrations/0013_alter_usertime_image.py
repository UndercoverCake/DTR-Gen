# Generated by Django 4.1.7 on 2023-05-07 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_usertime_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertime',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images'),
        ),
    ]