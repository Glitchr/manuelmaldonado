# Generated by Django 4.1.5 on 2023-02-12 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_websites', '0006_alter_certification_cert_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField()),
                ('is_opensource', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='is_opensource',
        ),
        migrations.RemoveField(
            model_name='project',
            name='is_published',
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_websites.portfolio'),
        ),
    ]
