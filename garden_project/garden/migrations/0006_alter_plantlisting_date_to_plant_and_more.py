# Generated by Django 4.2 on 2023-04-07 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0005_alter_calendar_comments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantlisting',
            name='date_to_plant',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='frost_tolerance',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='water_needs',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]