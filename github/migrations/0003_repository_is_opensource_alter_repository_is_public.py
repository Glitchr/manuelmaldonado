# Generated by Django 4.1.5 on 2023-03-11 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0002_alter_repository_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='is_opensource',
            field=models.BooleanField(blank=True, default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='repository',
            name='is_public',
            field=models.BooleanField(blank=True),
        ),
    ]
