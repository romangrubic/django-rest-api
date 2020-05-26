# Generated by Django 3.0.6 on 2020-05-26 11:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200526_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='JavaScript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('question_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Python',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('question_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='qanda',
            name='field_type',
        ),
        migrations.DeleteModel(
            name='ProgrammingField',
        ),
        migrations.DeleteModel(
            name='QandA',
        ),
    ]
