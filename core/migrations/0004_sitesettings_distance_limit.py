# Generated by Django 4.0.6 on 2022-07-08 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_image_is_processed'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='distance_limit',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
