# Generated by Django 5.0 on 2023-12-05 18:22

import myapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(default=myapp.models.increment_booking_number, editable=False, max_length=20)),
            ],
        ),
    ]
