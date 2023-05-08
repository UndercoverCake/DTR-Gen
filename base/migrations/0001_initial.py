# Generated by Django 4.1.7 on 2023-03-18 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='userTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField(blank=True, null=True)),
                ('month_name', models.CharField(blank=True, max_length=100, null=True)),
                ('monday_morning_time_in', models.CharField(blank=True, max_length=100, null=True)),
                ('monday_morning_time_out', models.CharField(blank=True, max_length=100, null=True)),
                ('monday_afternoon_time_in', models.CharField(blank=True, max_length=100, null=True)),
                ('monday_afternoon_time_out', models.CharField(blank=True, max_length=100, null=True)),
                ('tuesday_morning_time_in', models.CharField(blank=True, max_length=100, null=True)),
                ('tuesday_morning_time_out', models.CharField(blank=True, max_length=100, null=True)),
                ('tuesday_afternoon_time_in', models.CharField(blank=True, max_length=100, null=True)),
                ('tuesday_afternoon_time_out', models.CharField(blank=True, max_length=100, null=True)),
                ('wednesday_morning_time_in', models.CharField(blank=True, max_length=100, null=True)),
                ('wednesday_morning_time_out', models.CharField(blank=True, max_length=100, null=True)),
                ('wednesday_afternoon_time_in', models.CharField(blank=True, max_length=100, null=True)),
                ('wednesday_afternoon_time_out', models.CharField(blank=True, max_length=100, null=True)),
                ('thursday_morning_time_in', models.CharField(blank=True, max_length=100, null=True)),
                ('thursday_morning_time_out', models.CharField(blank=True, max_length=100, null=True)),
                ('thursday_afternoon_time_in', models.CharField(blank=True, max_length=100, null=True)),
                ('thursday_afternoon_time_out', models.CharField(blank=True, max_length=100, null=True)),
                ('friday_morning_time_in', models.CharField(blank=True, max_length=100, null=True)),
                ('friday_morning_time_out', models.CharField(blank=True, max_length=100, null=True)),
                ('friday_afternoon_time_in', models.CharField(blank=True, max_length=100, null=True)),
                ('friday_afternoon_time_out', models.CharField(blank=True, max_length=100, null=True)),
                ('saturday_morning_time_in', models.CharField(blank=True, max_length=100, null=True)),
                ('saturday_morning_time_out', models.CharField(blank=True, max_length=100, null=True)),
                ('saturday_afternoon_time_in', models.CharField(blank=True, max_length=100, null=True)),
                ('saturday_afternoon_time_out', models.CharField(blank=True, max_length=100, null=True)),
                ('sunday_morning_time_in', models.CharField(blank=True, max_length=100, null=True)),
                ('sunday_morning_time_out', models.CharField(blank=True, max_length=100, null=True)),
                ('sunday_afternoon_time_in', models.CharField(blank=True, max_length=100, null=True)),
                ('sunday_afternoon_time_out', models.CharField(blank=True, max_length=100, null=True)),
                ('monday_time_in_morning_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('monday_time_out_morning_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('monday_time_in_afternoon_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('monday_time_out_afternoon_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('tuesday_time_in_morning_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('tuesday_time_out_morning_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('tuesday_time_in_afternoon_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('tuesday_time_out_afternoon_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('wednesday_time_in_morning_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('wednesday_time_out_morning_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('wednesday_time_in_afternoon_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('wednesday_time_out_afternoon_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('thursday_time_in_morning_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('thursday_time_out_morning_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('thursday_time_in_afternoon_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('thursday_time_out_afternoon_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('friday_time_in_morning_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('friday_time_out_morning_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('friday_time_in_afternoon_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('friday_time_out_afternoon_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('saturday_time_in_morning_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('saturday_time_out_morning_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('saturday_time_in_afternoon_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('saturday_time_out_afternoon_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('sunday_time_in_morning_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('sunday_time_out_morning_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('sunday_time_in_afternoon_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('sunday_time_out_afternoon_overload', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]