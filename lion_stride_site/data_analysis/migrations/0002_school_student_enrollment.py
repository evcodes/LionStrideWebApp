# Generated by Django 3.0.3 on 2020-02-15 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_analysis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='student_enrollment',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
