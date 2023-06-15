# Generated by Django 4.2.1 on 2023-05-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='courseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
                ('course_code', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tbl_courses',
            },
        ),
    ]
