# Generated by Django 4.0.6 on 2022-07-12 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_sitesettings_distance_limit'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fire_info', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
