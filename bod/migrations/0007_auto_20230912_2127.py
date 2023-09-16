# Generated by Django 3.0.6 on 2023-09-12 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bod', '0006_auto_20230912_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='category',
            field=models.CharField(choices=[('名詞', '名詞'), ('代詞', '代詞'), ('動詞', '動詞'), ('形容詞', '形容詞'), ('副詞', '副詞'), ('連詞', '連詞'), ('助詞', '助詞'), ('後綴', '後綴'), ('小品詞', '小品詞'), ('語氣詞', '語氣詞'), ('片語', '片語'), ('例文例句', '例文例句')], max_length=20, verbose_name='品詞'),
        ),
    ]
