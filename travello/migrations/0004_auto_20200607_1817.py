# Generated by Django 3.0.6 on 2020-06-07 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_travel_history2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medical_history',
            old_name='Bronchitis',
            new_name='bronchitis',
        ),
        migrations.RenameField(
            model_name='medical_history',
            old_name='COPD',
            new_name='copd',
        ),
        migrations.RenameField(
            model_name='medical_history',
            old_name='Diabetes_mellitus',
            new_name='diabetes_mellitus',
        ),
        migrations.RenameField(
            model_name='medical_history',
            old_name='HIV_AIDS',
            new_name='hiv_aids',
        ),
        migrations.RenameField(
            model_name='medical_history',
            old_name='Ischemic_heart_disease',
            new_name='ischemic_heart_disease',
        ),
        migrations.RenameField(
            model_name='medical_history',
            old_name='Kidney_Disease',
            new_name='kidney_disease',
        ),
        migrations.RenameField(
            model_name='medical_history',
            old_name='Stroke',
            new_name='stroke',
        ),
    ]
