# Generated by Django 3.2.4 on 2021-07-27 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('text', models.TextField()),
                ('service', models.TextField()),
                ('service_icon', models.ImageField(upload_to='')),
                ('feature_title', models.TextField()),
                ('feature_body', models.TextField()),
                ('feature_icon', models.ImageField(upload_to='')),
                ('feature_url', models.TextField()),
            ],
        ),
    ]
