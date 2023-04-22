# Generated by Django 4.2 on 2023-04-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0006_alter_plantlisting_date_to_plant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='comments',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='fertilize_dates',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='frost_dates',
            field=models.CharField(default='no frost date', max_length=100),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='harvest_times',
            field=models.CharField(default='no harvest time', max_length=100),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='plant_dates',
            field=models.CharField(default='no plant date', max_length=100),
        ),
        migrations.AlterField(
            model_name='plant',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='date_to_plant',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='frost_tolerance',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='germination_time',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='grow_from_seed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='grow_from_transplant',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='harvest_times',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='plant_needs_fertilization',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='season',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='seed_depth',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='sunlight_needs',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='water_needs',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]