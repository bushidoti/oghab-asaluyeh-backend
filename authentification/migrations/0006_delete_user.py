# Generated by Django 4.2 on 2023-05-07 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0005_rename_users_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
