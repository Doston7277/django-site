# Generated by Django 3.2.4 on 2021-07-27 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_feature_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='')),
                ('about_title', models.TextField()),
                ('about_body', models.TextField()),
                ('about_text', models.TextField()),
                ('subscribe_title', models.TextField()),
                ('subscribe_body', models.TextField()),
                ('project_title', models.TextField()),
                ('project_body', models.TextField()),
                ('team_title', models.TextField()),
                ('team_body', models.TextField()),
                ('contact_title', models.TextField()),
                ('contact_body', models.TextField()),
                ('contact_phone', models.TextField()),
                ('contact_phone_icon', models.ImageField(upload_to='')),
                ('contact_email', models.TextField()),
                ('contact_email_icon', models.ImageField(upload_to='')),
                ('contact_site', models.TextField()),
                ('contact_site_icon', models.ImageField(upload_to='')),
                ('footer_text', models.TextField()),
                ('footer_instagram_url', models.TextField()),
                ('footer_instagram_icon', models.ImageField(upload_to='')),
                ('footer_telegram_url', models.TextField()),
                ('footer_telegram_icon', models.ImageField(upload_to='')),
                ('footer_facebook_url', models.TextField()),
                ('footer_facebook_icon', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='About',
        ),
    ]
