# Generated by Django 4.2.1 on 2023-06-16 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_students', '0002_rename_courses_studentmodel_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='students/profiles'),
        ),
    ]