# Generated by Django 5.1.5 on 2025-02-05 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmConnectApp', '0002_alter_consumermodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumermodel',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
