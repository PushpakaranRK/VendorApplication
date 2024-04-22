# Generated by Django 5.0.3 on 2024-04-17 23:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(null=True)),
                ('website', models.TextField(blank=True, null=True)),
                ('established_year', models.CharField(default='1964', max_length=10)),
                ('location_countries', models.JSONField(blank=True, null=True)),
                ('location_cities', models.JSONField(blank=True, null=True)),
                ('contact_telephone', models.JSONField(blank=True, null=True)),
                ('address', models.JSONField(blank=True, null=True)),
                ('employee_count', models.CharField(blank=True, max_length=255, null=True)),
                ('has_internal_professional_services', models.BooleanField(blank=True, null=True)),
                ('last_demo_date', models.DateField(blank=True, null=True)),
                ('last_reviewed_date', models.DateField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='media/company_logos/')),
            ],
            options={
                'verbose_name_plural': 'Companies',
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=30, unique=True)),
                ('category_description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Product Categories',
                'db_table': 'product_category',
                'indexes': [models.Index(fields=['category_name'], name='category_name_idx')],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('cloud_type', models.CharField(max_length=100)),
                ('business_areas', models.CharField(max_length=255)),
                ('modules', models.TextField(null=True)),
                ('financial_services_client_types', models.CharField(max_length=255, null=True)),
                ('additional_information', models.TextField(null=True)),
                ('is_document_attached', models.BooleanField(default=False)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='media/product_logos/')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.company')),
                ('categories', models.ManyToManyField(related_name='products', to='admin_app.productcategory')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'db_table': 'products',
                'indexes': [models.Index(fields=['company'], name='company_idx'), models.Index(fields=['name'], name='product_name_idx')],
            },
        ),
    ]
