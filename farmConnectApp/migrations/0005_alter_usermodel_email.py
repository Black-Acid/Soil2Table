# Generated by Django 5.1.5 on 2025-02-14 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmConnectApp', '0004_alter_usermodel_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
