# Generated by Django 4.1.5 on 2023-01-18 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_websites', '0004_language'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'verbose_name_plural': 'Education'},
        ),
        migrations.AlterModelOptions(
            name='socialmedia',
            options={'verbose_name_plural': 'Social Media'},
        ),
    ]