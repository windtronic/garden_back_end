# Generated by Django 4.2 on 2023-04-13 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0010_rename_address_user_user_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_password',
            new_name='password',
        ),
    ]