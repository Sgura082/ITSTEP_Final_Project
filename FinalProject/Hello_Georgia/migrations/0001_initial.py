# Generated by Django 5.0.6 on 2024-06-30 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guide_ID', models.CharField(max_length=11)),
                ('guide_name', models.CharField(max_length=30)),
                ('guide_last_name', models.CharField(max_length=30)),
                ('guide_mobiluri', models.CharField(max_length=10)),
                ('guide_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number_of_tours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tester_name', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_name', models.CharField(max_length=30)),
                ('tour_length_days', models.IntegerField()),
                ('tour_start_date', models.DateField()),
                ('tour_max_visitorN', models.IntegerField()),
                ('tour_current_visitorN', models.IntegerField()),
                ('tour_free_spots', models.IntegerField()),
                ('tour_guide', models.ManyToManyField(to='Hello_Georgia.guide')),
                ('tour_region', models.ManyToManyField(to='Hello_Georgia.region')),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_ID', models.CharField(max_length=20)),
                ('visitor_name', models.CharField(max_length=30)),
                ('visitor_last_name', models.CharField(max_length=30)),
                ('visitor_mobiluri', models.CharField(max_length=9)),
                ('chosen_tour', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Hello_Georgia.tour')),
            ],
        ),
    ]
