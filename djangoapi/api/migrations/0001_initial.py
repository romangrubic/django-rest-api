# Generated by Django 3.0.6 on 2020-05-26 10:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProgrammingField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='QandA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('field_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.ProgrammingField')),
            ],
        ),
    ]