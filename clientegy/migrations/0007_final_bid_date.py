# Generated by Django 3.1.3 on 2020-11-30 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientegy', '0006_remove_final_bid_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='final_bid',
            name='date',
            field=models.TextField(default=None),
        ),
    ]
