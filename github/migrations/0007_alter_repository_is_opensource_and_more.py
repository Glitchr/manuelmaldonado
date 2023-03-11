# Generated by Django 4.1.5 on 2023-03-11 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0006_alter_repository_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='is_opensource',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='repository',
            name='is_public',
            field=models.BooleanField(),
        ),
    ]