# Generated by Django 5.0.6 on 2024-05-17 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='comment',
            new_name='comments',
        ),
    ]
