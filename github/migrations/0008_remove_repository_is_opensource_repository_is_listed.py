# Generated by Django 4.1.5 on 2023-03-11 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0007_alter_repository_is_opensource_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repository',
            name='is_opensource',
        ),
        migrations.AddField(
            model_name='repository',
            name='is_listed',
            field=models.BooleanField(default=True),
        ),
    ]