# Generated by Django 4.1.3 on 2022-11-21 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_parent_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='id',
        ),
        migrations.AlterField(
            model_name='child',
            name='child_registration_no',
            field=models.CharField(default='some_value', max_length=50, primary_key=True, serialize=False),
        ),
    ]