# Generated by Django 4.1.7 on 2023-03-19 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_usertime_first_name_usertime_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertime',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]