# Generated by Django 5.1.3 on 2024-12-20 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_pages', '0004_alter_news_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
            ],
        ),
    ]
