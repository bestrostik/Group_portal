# Generated by Django 5.1.3 on 2024-12-22 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_pages', '0009_alter_notification_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsefulLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'permissions': [('can_add_useful_link', 'Can add useful link'), ('can_edit_useful_link', 'Can edit useful link'), ('can_delete_useful_link', 'Can delete useful link')],
            },
        ),
        migrations.RemoveField(
            model_name='notification',
            name='creater',
        ),
    ]