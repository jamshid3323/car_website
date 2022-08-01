# Generated by Django 4.0.6 on 2022-08-01 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_featuredcarmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('subject', models.CharField(max_length=50, verbose_name='subject')),
                ('message', models.TextField(verbose_name='message')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
            },
        ),
    ]