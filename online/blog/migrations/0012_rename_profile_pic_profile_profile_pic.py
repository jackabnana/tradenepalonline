# Generated by Django 3.2.5 on 2021-07-12 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20210711_0753'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Profile_pic',
            new_name='profile_pic',
        ),
    ]
