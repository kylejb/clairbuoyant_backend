# Generated by Django 3.1.3 on 2021-01-19 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buoyant', '0002_auto_20201202_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meteorological',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observation_date', models.DateTimeField()),
                ('wind_dir', models.PositiveSmallIntegerField()),
                ('wind_speed', models.DecimalField(decimal_places=1, max_digits=5)),
                ('wind_gust', models.DecimalField(decimal_places=1, max_digits=5)),
                ('wave_height', models.DecimalField(decimal_places=1, max_digits=5)),
                ('dom_wave_period', models.DecimalField(decimal_places=1, max_digits=5)),
                ('avg_wave_period', models.DecimalField(decimal_places=1, max_digits=5)),
                ('wave_dir', models.PositiveSmallIntegerField()),
                ('sea_pressure', models.DecimalField(decimal_places=1, max_digits=5)),
                ('air_temp', models.DecimalField(decimal_places=1, max_digits=5)),
                ('sea_temp', models.DecimalField(decimal_places=1, max_digits=5)),
                ('tide', models.CharField(max_length=6)),
                ('dewpoint_temp', models.DecimalField(decimal_places=1, max_digits=5)),
                ('station_visibility', models.DecimalField(decimal_places=1, max_digits=5)),
                ('pressure_tendency', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('buoy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buoyant.buoy')),
            ],
        ),
        migrations.DeleteModel(
            name='Observation',
        ),
    ]
