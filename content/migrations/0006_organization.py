# Generated by Django 5.0.4 on 2024-04-22 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_alter_news_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.TextField(blank=True, max_length=100, null=True)),
                ('logo', models.ImageField(blank=True, upload_to='logo_image/')),
                ('address', models.TextField(blank=True, max_length=100, null=True)),
                ('contact', models.TextField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('facebook', models.TextField(blank=True, max_length=100, null=True)),
                ('twiter', models.TextField(blank=True, max_length=100, null=True)),
                ('instagram', models.TextField(blank=True, max_length=100, null=True)),
                ('linkdin', models.TextField(blank=True, max_length=100, null=True)),
                ('youtube', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
