# Generated by Django 3.2.8 on 2021-10-24 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hexoweb', '0003_auto_20211022_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2147483647)),
                ('url', models.CharField(max_length=2147483647)),
                ('size', models.CharField(max_length=2147483647)),
                ('date', models.CharField(max_length=2147483647)),
                ('type', models.CharField(max_length=2147483647)),
            ],
        ),
    ]