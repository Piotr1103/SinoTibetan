# Generated by Django 3.0.6 on 2023-08-19 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bod', '0003_word_transliteration'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='category',
            field=models.CharField(default='...', max_length=20),
        ),
        migrations.AlterField(
            model_name='word',
            name='bod',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='word',
            name='han',
            field=models.TextField(),
        ),
    ]
