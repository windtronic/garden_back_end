# Generated by Django 4.2 on 2023-04-07 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0004_plantlisting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='comments',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='fertilize_dates',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='frost_dates',
            field=models.CharField(blank=True, default='no frost date', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='harvest_times',
            field=models.CharField(blank=True, default='no harvest time', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='plant_dates',
            field=models.CharField(blank=True, default='no plant date', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='date_to_plant',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='frost_tolerance',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='germination_time',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='grow_from_seed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='grow_from_transplant',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='harvest_times',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='plant_needs_fertilization',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='row_spacing',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='season',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='seed_depth',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='sunlight_needs',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='plantlisting',
            name='water_needs',
            field=models.TextField(blank=True, default=''),
        ),
    ]