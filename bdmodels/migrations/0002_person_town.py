# Generated by Django 4.2.5 on 2023-09-06 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmodels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='town',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]