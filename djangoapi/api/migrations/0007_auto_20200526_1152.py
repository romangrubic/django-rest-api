# Generated by Django 3.0.6 on 2020-05-26 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200526_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='javascript',
            name='answer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='python',
            name='answer',
            field=models.TextField(),
        ),
    ]
