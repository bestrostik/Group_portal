# Generated by Django 5.1.3 on 2024-12-22 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('default_pages', '0008_alter_event_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'permissions': [('can_create_notification', 'Can create notification'), ('can_modify_notification', 'Can modify notification')]},
        ),
    ]
