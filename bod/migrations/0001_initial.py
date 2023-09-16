# Generated by Django 3.0.6 on 2023-08-16 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bod', models.CharField(max_length=40)),
                ('han', models.CharField(max_length=40)),
                ('rme', models.CharField(max_length=40)),
                ('nuo', models.CharField(max_length=40)),
                ('nax', models.CharField(max_length=40)),
                ('pam', models.CharField(max_length=40)),
                ('pronunciation', models.CharField(max_length=40)),
                ('explanation', models.TextField()),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
