# Generated by Django 5.0.6 on 2024-06-19 09:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('isbn', models.IntegerField()),
                ('published_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
