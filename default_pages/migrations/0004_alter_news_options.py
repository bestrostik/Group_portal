# Generated by Django 5.1.3 on 2024-11-24 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('default_pages', '0003_alter_news_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'permissions': [('can_post_news', 'Can post news')]},
        ),
    ]