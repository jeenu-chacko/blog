# Generated by Django 3.1.4 on 2020-12-20 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_profile_linkedin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='linkedin',
            new_name='linkedin_url',
        ),
    ]
