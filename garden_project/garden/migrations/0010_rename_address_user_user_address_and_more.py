# Generated by Django 4.2 on 2023-04-13 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0009_rename_user_address_user_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='address',
            new_name='user_address',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='user_email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='user_password',
        ),
    ]
