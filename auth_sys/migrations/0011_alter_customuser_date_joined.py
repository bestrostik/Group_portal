# Generated by Django 5.1.3 on 2024-12-15 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_sys', '0010_customuser_birth_day_customuser_birth_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
