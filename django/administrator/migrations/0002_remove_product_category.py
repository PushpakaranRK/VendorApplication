# Generated by Django 5.0.2 on 2024-04-09 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
