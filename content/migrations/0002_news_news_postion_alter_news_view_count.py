# Generated by Django 5.0.4 on 2024-04-14 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_postion',
            field=models.CharField(choices=[('normal', 'Normal'), ('first', 'First'), ('second', 'Second'), ('third', 'Third'), ('forth', 'Forth')], default='normal', max_length=100),
        ),
        migrations.AlterField(
            model_name='news',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
