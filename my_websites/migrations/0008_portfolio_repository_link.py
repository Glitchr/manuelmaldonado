# Generated by Django 4.1.5 on 2023-02-12 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_websites', '0007_portfolio_remove_project_is_opensource_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='repository_link',
            field=models.URLField(blank=True),
        ),
    ]