# Generated by Django 4.1.3 on 2022-11-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccine',
            name='expiry_date',
            field=models.DateTimeField(null=True),
        ),
    ]
