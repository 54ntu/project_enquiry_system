# Generated by Django 4.2.1 on 2023-05-17 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmodel',
            old_name='courses',
            new_name='course',
        ),
    ]
