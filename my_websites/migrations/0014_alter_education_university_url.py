# Generated by Django 4.1.5 on 2023-02-13 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_websites', '0013_alter_education_is_completed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='university_url',
            field=models.URLField(blank=True),
        ),
    ]
