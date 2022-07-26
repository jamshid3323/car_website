# Generated by Django 4.0.6 on 2022-07-26 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PopularCarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, verbose_name='brand')),
                ('image', models.ImageField(upload_to='popular_car/', verbose_name='image')),
                ('model', models.CharField(max_length=30, verbose_name='model')),
                ('condition', models.CharField(max_length=30, verbose_name='condition')),
                ('year', models.CharField(max_length=4, verbose_name='year')),
                ('motor_type', models.CharField(max_length=30, verbose_name='motor type')),
                ('fuel', models.CharField(max_length=30, verbose_name='fuel')),
                ('price', models.DecimalField(decimal_places=3, max_digits=6, verbose_name='price')),
                ('max_speed', models.CharField(max_length=3, verbose_name='maximal speed')),
                ('is_active', models.BooleanField(blank=True, default=False, verbose_name='is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
        ),
    ]